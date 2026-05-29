#!/usr/bin/env python3
"""
main.py — CLI for the RAG Agent

Commands:
  python main.py ingest          # load docs → split → embed → store in Chroma
  python main.py ask "<question>" # single question
  python main.py chat             # interactive REPL
  python main.py demo             # run 3 showcase questions
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def cmd_ingest():
    from ingest.pipeline import ingest
    ingest(reset=True)


def cmd_ask(question: str, graph=None):
    from agent.graph import run_agent, build_graph
    g = graph or build_graph()
    print(f"\n{'='*60}\nQ: {question}\n{'='*60}")
    result = run_agent(question, graph=g)
    print(f"\nA: {result['answer']}\n")
    return g


def cmd_chat():
    from agent.graph import build_graph, run_agent
    print("\n🤖 RAG Agent — interactive  (type 'exit' to quit)\n")
    graph = build_graph()
    while True:
        try:
            q = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not q or q.lower() in {"exit", "quit"}:
            break
        result = run_agent(q, graph=graph)
        print(f"\nAgent: {result['answer']}\n")


def cmd_demo():
    from agent.graph import build_graph
    graph = build_graph()
    questions = [
        "What is Retrieval-Augmented Generation (RAG) and what problem does it solve?",
        "What is the difference between supervised and unsupervised learning?",
        "What is 2 to the power of 16, and which Python library handles numerical arrays?",
    ]
    for q in questions:
        cmd_ask(q, graph=graph)


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    cmd = args[0]
    if cmd == "ingest":
        cmd_ingest()
    elif cmd == "ask":
        if len(args) < 2:
            print("Usage: python main.py ask '<question>'")
            sys.exit(1)
        cmd_ask(args[1])
    elif cmd == "chat":
        cmd_chat()
    elif cmd == "demo":
        cmd_demo()
    else:
        print(f"Unknown command: {cmd}. Use: ingest | ask | chat | demo")
        sys.exit(1)
