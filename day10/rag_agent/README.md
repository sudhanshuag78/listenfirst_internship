# 📚 Chat with Documents — RAG + LangGraph + MistralAI

A document Q&A agent built with **LangChain-native** components, **LangGraph** for orchestration, and **Mistral AI** for both embeddings and chat.

---

## Architecture

```
User query
    │
    ▼
┌─────────────────────────────────────────────────┐
│              LangGraph Agent                    │
│                                                 │
│  ┌─────────┐  tool_calls?  ┌──────────────────┐│
│  │  agent  │──── yes ─────►│    retrieve      ││
│  │Mistral  │◄──────────────│  (ToolNode)      ││
│  │  LLM    │               └──────────────────┘│
│  └─────────┘                                   │
│       │ no tool_calls                          │
│       ▼                                        │
│     [END]                                      │
└─────────────────────────────────────────────────┘
         │                        │
  ┌──────▼──────┐         ┌───────▼──────┐
  │   Chroma    │         │  Calculator  │
  │  Vectorstore│         │  MCP Server  │
  │(mistral-    │         │  :8765       │
  │  embed)     │         └──────────────┘
  └─────────────┘
```

### LangChain Pipeline (ingest)
```
DirectoryLoader  →  RecursiveCharacterTextSplitter  →  MistralAIEmbeddings  →  Chroma
```

### LangGraph Nodes
| Node | Role |
|---|---|
| `agent` | `ChatMistralAI` with bound tools — decides to retrieve, calculate, or answer |
| `retrieve` | `ToolNode` — executes whichever tool(s) the agent called |
| `END` | Final answer returned to the user |

### Conditional Edge
After every `agent` step: `tool_calls present` → **retrieve** · `no tool_calls` → **END**

---

## Module Layout

```
rag_agent/
├── docs/
│   ├── ai_ml_concepts.md
│   ├── python_guide.md
│   └── llm_agents.md
│
├── ingest/
│   └── pipeline.py      # DirectoryLoader → splitter → MistralAIEmbeddings → Chroma
│
├── agent/
│   ├── tools.py         # @tool: retrieve_docs (Chroma retriever) + calculator
│   └── graph.py         # LangGraph StateGraph wired to ChatMistralAI
│
├── server/
│   └── mcp_server.py    # FastAPI MCP-compatible calculator server (:8765)
│
├── main.py              # CLI: ingest | ask | chat | demo
├── requirements.txt
└── .env.example
```

---

## Setup (one-line per step)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your Mistral API key
export MISTRAL_API_KEY=your_key_here
# or: copy .env.example → .env and fill in the key

# 3. Ingest documents (calls Mistral embed API, writes to ./chroma_db)
python main.py ingest

# 4. Ask a question
python main.py ask "What is RAG and how does it reduce hallucination?"

# 5. Interactive chat
python main.py chat

# 6. Run all 3 demo questions
python main.py demo

# 7. (Optional) Start the MCP calculator server
python server/mcp_server.py
```

---

## Example Questions

### Q1 — RAG (retrieves from `llm_agents.md`)
```
python main.py ask "What is Retrieval-Augmented Generation and what problem does it solve?"
```
**Expected:** Explanation that RAG combines LLMs with retrieval, reducing hallucination by conditioning on retrieved documents.
**Sources:** `[llm_agents.md, start_index=N]`

---

### Q2 — Cross-document synthesis (`ai_ml_concepts.md`)
```
python main.py ask "What is the difference between supervised and unsupervised learning?"
```
**Expected:** Supervised = labeled data → mapping function; Unsupervised = hidden patterns in unlabeled data.
**Sources:** `[ai_ml_concepts.md, start_index=N]`

---

### Q3 — Hybrid: calculator + RAG (`python_guide.md`)
```
python main.py ask "What is 2 to the power of 16, and which Python library handles numerical arrays?"
```
**Expected:** `2 ** 16 = 65536` (via calculator) + NumPy explanation (via retrieval).
**Sources:** calculator, `[python_guide.md, start_index=N]`

---

## MCP Tool

The **calculator** is registered in two ways:

| Mode | File | How it's used |
|------|------|---------------|
| LangGraph tool (in-process) | `agent/tools.py` | Called by `ToolNode` during agent execution — zero latency |
| MCP HTTP server | `server/mcp_server.py` | Exposes the same function over `POST /tools/call` for any MCP client |

**MCP tradeoff:** Running in-process is simpler and faster for a single agent. A true MCP stdio/SSE transport (via the `mcp` Python SDK) would make the tool reusable across multiple agents and languages. The HTTP server in `/server` bridges the gap — same contract, HTTP transport instead of stdio.

---

## Live Modifications (Demo Cheat Sheet)

| Change | Where |
|--------|-------|
| Adjust `top_k` | `ingest/pipeline.py` → `TOP_K` constant, or `get_retriever(top_k=N)` |
| Add a new document | Drop file in `docs/`, run `python main.py ingest` |
| Change chunk size | `ingest/pipeline.py` → `CHUNK_SIZE` / `CHUNK_OVERLAP` |
| Swap LLM model | `agent/graph.py` → `build_graph(model="mistral-small-latest")` |
| Add a new tool | Add `@tool` in `agent/tools.py`, append to `ALL_TOOLS` |

---

## Tech Stack

| Component | Library / Model |
|---|---|
| LLM | `mistral-large-latest` via `langchain-mistralai` |
| Embeddings | `mistral-embed` via `MistralAIEmbeddings` |
| Document loading | `langchain-community` `DirectoryLoader` + `TextLoader` |
| Chunking | `langchain-text-splitters` `RecursiveCharacterTextSplitter` |
| Vector store | `langchain-chroma` `Chroma` (persistent) |
| Agent orchestration | `langgraph` `StateGraph` |
| MCP server | `fastapi` + `uvicorn` |
