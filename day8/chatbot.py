from typing import TypedDict
from dotenv import load_dotenv

from langgraph.graph import StateGraph, START, END
from langchain_mistralai import ChatMistralAI


# -------------------------
# load env
# -------------------------
load_dotenv()


# -------------------------
# mistral model
# -------------------------
llm = ChatMistralAI(
    model="mistral-small-latest"
)


# -------------------------
# state
# -------------------------
class ChatState(TypedDict):
    message: str
    response: str


# -------------------------
# chatbot node
# -------------------------
def chatbot_node(state: ChatState):
    user_message = state["message"]

    result = llm.invoke(user_message)

    return {
        "response": result.content
    }


# -------------------------
# build graph
# -------------------------
graph_builder = StateGraph(ChatState)

graph_builder.add_node("chatbot", chatbot_node)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()


# -------------------------
# run
# -------------------------
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Bye 👋")
        break

    result = graph.invoke(
        {
            "message": user_input,
            "response": "",
        }
    )

    print("Bot:", result["response"])