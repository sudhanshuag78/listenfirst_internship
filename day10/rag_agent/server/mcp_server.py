"""
server/mcp_server.py
---------------------
MCP-compatible HTTP server that exposes the calculator tool.

Endpoints (JSON-RPC style, matching MCP spec):
  GET  /tools/list    → tool manifest
  POST /tools/call    → execute a tool

Run:
    python server/mcp_server.py

Example:
    curl http://localhost:8765/tools/list
    curl -X POST http://localhost:8765/tools/call \
         -H "Content-Type: application/json" \
         -d '{"name": "calculator", "arguments": {"expression": "sqrt(2)*100"}}'

MCP tradeoff:
  Full MCP uses stdio or SSE transport with JSON-RPC 2.0 framing and the
  official `mcp` Python SDK. This server implements the same tool contract
  over plain HTTP — the tool logic is identical, only the transport differs.
  Switching to true MCP stdio: wrap this in `mcp.server.Server` and replace
  uvicorn with `mcp.run()`. The agent in /agent/tools.py calls the same
  function in-process for zero-latency demo use.
"""

import ast
import math
from typing import Any

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Calculator MCP Server", version="1.0.0")

# ── Safe eval (self-contained so server has no project deps) ──────────────────

_ALLOWED = {
    ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant,
    ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod,
    ast.FloorDiv, ast.USub, ast.UAdd, ast.Call, ast.Attribute,
    ast.Name, ast.Load,
}
_NAMES = {
    "abs": abs, "round": round,
    "sqrt": math.sqrt, "log": math.log, "log10": math.log10,
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "pi": math.pi, "e": math.e, "ceil": math.ceil, "floor": math.floor,
}


def _safe_eval(expr: str) -> float:
    tree = ast.parse(expr.strip(), mode="eval")
    for node in ast.walk(tree):
        if type(node) not in _ALLOWED:
            raise ValueError(f"Disallowed: {type(node).__name__}")
    return eval(compile(tree, "<string>", "eval"), {"__builtins__": {}}, _NAMES)  # noqa: S307


# ── MCP endpoints ─────────────────────────────────────────────────────────────

MANIFEST = {
    "tools": [{
        "name": "calculator",
        "description": (
            "Evaluate a math expression. "
            "Supports +,-,*,/,**,%,//,sqrt,log,log10,sin,cos,tan,pi,e,abs,round,ceil,floor."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "expression": {"type": "string", "description": "e.g. 'sqrt(144)' or '2**10'"}
            },
            "required": ["expression"],
        },
    }]
}


class ToolCallRequest(BaseModel):
    name: str
    arguments: dict[str, Any]


@app.get("/tools/list")
async def list_tools():
    return MANIFEST


@app.post("/tools/call")
async def call_tool(req: ToolCallRequest):
    if req.name != "calculator":
        raise HTTPException(status_code=404, detail=f"Unknown tool: {req.name}")
    expr = req.arguments.get("expression", "")
    if not expr:
        raise HTTPException(status_code=400, detail="'expression' required")
    try:
        result = _safe_eval(expr)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return {"content": [{"type": "text", "text": f"{expr} = {result}"}], "isError": False}
    except Exception as exc:
        return {"content": [{"type": "text", "text": f"Error: {exc}"}], "isError": True}


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    print("Calculator MCP Server → http://localhost:8765")
    uvicorn.run(app, host="0.0.0.0", port=8765)
