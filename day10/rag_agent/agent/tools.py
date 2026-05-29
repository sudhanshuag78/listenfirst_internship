"""
agent/tools.py
--------------
Two tools registered as LangChain tools so LangGraph's ToolNode can execute them:

  1. retrieve_docs  — wraps the LangChain Chroma retriever (RAG)
  2. calculator     — safe AST-based arithmetic evaluator

MCP note:
  `calculator` is also exposed as a standalone MCP-compatible HTTP server
  in /server/mcp_server.py.  As a LangGraph tool it runs in-process (zero
  latency); the MCP server makes the same function available to any MCP
  client over HTTP — same logic, different transport.
"""

import ast
import math

from langchain_core.tools import tool

from ingest.pipeline import get_retriever

# Lazy-loaded singleton retriever
_retriever = None


def _get_retriever():
    global _retriever
    if _retriever is None:
        _retriever = get_retriever()
    return _retriever


# ── Tool 1: Document Retrieval ────────────────────────────────────────────────

@tool
def retrieve_docs(query: str) -> str:
    """
    Search the document knowledge base for information relevant to the query.
    Returns the top matching chunks with their source filename and chunk index.
    Call this tool whenever the question requires factual information from documents.
    """
    retriever = _get_retriever()
    docs = retriever.invoke(query)          # standard LangChain retriever interface

    if not docs:
        return "No relevant documents found."

    parts = []
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "unknown")
        start  = doc.metadata.get("start_index", "?")
        parts.append(
            f"[Chunk {i}] source={source} | start_index={start}\n"
            f"{doc.page_content}"
        )
    return "\n\n---\n\n".join(parts)


# ── Tool 2: Calculator ────────────────────────────────────────────────────────

_ALLOWED_NODES = {
    ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant,
    ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod,
    ast.FloorDiv, ast.USub, ast.UAdd, ast.Call, ast.Attribute,
    ast.Name, ast.Load,
}

_SAFE_NAMES = {
    "abs": abs, "round": round,
    "sqrt": math.sqrt, "log": math.log, "log10": math.log10,
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "pi": math.pi, "e": math.e,
    "ceil": math.ceil, "floor": math.floor,
}


def _safe_eval(expr: str) -> float:
    tree = ast.parse(expr.strip(), mode="eval")
    for node in ast.walk(tree):
        if type(node) not in _ALLOWED_NODES:
            raise ValueError(f"Disallowed operation: {type(node).__name__}")
    return eval(compile(tree, "<string>", "eval"),  # noqa: S307
                {"__builtins__": {}}, _SAFE_NAMES)


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression and return the numeric result.
    Supports: +, -, *, /, **, %, //, sqrt, log, log10, sin, cos, tan, pi, e, abs, round, ceil, floor.
    Examples: "2 ** 16", "sqrt(144)", "sin(pi/2)", "log10(1000)", "round(pi, 4)".
    Use this tool whenever the user asks for any arithmetic or math calculation.
    """
    try:
        result = _safe_eval(expression)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return f"{expression} = {result}"
    except Exception as exc:
        return f"Calculator error: {exc}"


ALL_TOOLS = [retrieve_docs, calculator]
