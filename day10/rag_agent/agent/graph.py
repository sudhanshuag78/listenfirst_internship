"""
agent/graph.py
--------------
LangGraph agent graph wired to ChatMistralAI.

Graph topology:
                         conditional
  [START] → agent ──── tool_calls? ──── yes ──→ retrieve ─┐
                  └──── no ──→ [END]                       │
                  ←─────────────────────────────────────────┘

Nodes:
  agent     — ChatMistralAI with bound tools; decides what to do
  retrieve  — LangGraph ToolNode that executes retrieve_docs / calculator

Conditional edge:
  After every agent step, check last message:
    • has tool_calls  → go to 'retrieve'
    • no tool_calls   → go to END  (final answer)
"""

from typing import Annotated, Literal, TypedDict

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_mistralai import ChatMistralAI
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from agent.tools import ALL_TOOLS

# ── Agent state ───────────────────────────────────────────────────────────────

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# ── System prompt ─────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are a helpful research assistant with access to a \
document knowledge base and a calculator.

Rules:
1. When the question requires factual information, call retrieve_docs FIRST \
   to search the knowledge base before answering.
2. When the user asks for calculations or math, use the calculator tool.
3. Synthesise retrieved information into a clear, concise answer.
4. Always end your answer with a "Sources:" section listing every document \
   chunk you used, in this exact format:
       Sources: [filename, start_index=N]
5. If retrieved documents don't contain the answer, say so honestly.
"""

# ── Graph factory ─────────────────────────────────────────────────────────────

def build_graph(model: str = "mistral-large-latest") -> "CompiledGraph":
    """Build and return the compiled LangGraph agent."""

    llm = ChatMistralAI(
        model=model,
        temperature=0,
    ).bind_tools(ALL_TOOLS)

    tool_node = ToolNode(ALL_TOOLS)

    # ── Node: agent ───────────────────────────────────────────────────────────
    def agent_node(state: AgentState) -> AgentState:
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
        response = llm.invoke(messages)
        return {"messages": [response]}

    # ── Node: retrieve (tool executor) ────────────────────────────────────────
    def retrieve_node(state: AgentState) -> AgentState:
        return tool_node.invoke(state)

    # ── Conditional routing ───────────────────────────────────────────────────
    def should_continue(state: AgentState) -> Literal["retrieve", "end"]:
        last = state["messages"][-1]
        if hasattr(last, "tool_calls") and last.tool_calls:
            return "retrieve"
        return "end"

    # ── Assemble ──────────────────────────────────────────────────────────────
    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)
    graph.add_node("retrieve", retrieve_node)

    graph.set_entry_point("agent")

    graph.add_conditional_edges(
        "agent",
        should_continue,
        {"retrieve": "retrieve", "end": END},
    )
    graph.add_edge("retrieve", "agent")   # always return to agent after tool use

    return graph.compile()


# ── Convenience runner ────────────────────────────────────────────────────────

def run_agent(question: str, graph=None) -> dict:
    """Run the agent on a single question. Returns answer string."""
    if graph is None:
        graph = build_graph()

    final_state = graph.invoke({
        "messages": [HumanMessage(content=question)],
    })

    return {
        "answer": final_state["messages"][-1].content,
        "messages": final_state["messages"],
    }
