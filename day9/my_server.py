# my_server.py

from mcp.server.fastmcp import FastMCP
import os

# Server ka naam
mcp = FastMCP("My First MCP Server")


@mcp.tool()
def calculator(operation: str, a: float, b: float) -> str:
    """
    Basic calculator.
    operation: add / subtract / multiply / divide
    """

    if operation == "add":
        return str(a + b)

    elif operation == "subtract":
        return str(a - b)

    elif operation == "multiply":
        return str(a * b)

    elif operation == "divide":

        if b == 0:
            return "Error: Zero se divide nahi kar sakte!"

        return str(a / b)

    else:
        return "Error: Invalid operation"


@mcp.tool()
def read_file(filepath: str) -> str:
    """
    File ka content padhta hai
    """

    # file exist karti hai ya nahi
    if not os.path.exists(filepath):
        return "Error: File nahi mili"

    # agar hai to read karo
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    return content


if __name__ == "__main__":
    mcp.run()