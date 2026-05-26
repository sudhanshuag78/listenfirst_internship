from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    AIMessage,
    SystemMessage,
    HumanMessage,
)

# Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.9
)

# System instruction
messages = [
    SystemMessage(
        content="You are a funny AI assistant."
    )
]

print("---------- Welcome (type 0 to exit) ----------")

while True:

    prompt = input("You: ")

    if prompt == "0":
        break

    # user message
    messages.append(
        HumanMessage(content=prompt)
    )

    # Gemini response
    response = model.invoke(messages)

    # save memory
    messages.append(
        AIMessage(content=response.content)
    )

    print("Bot:", response.content)

print("\nConversation ended.")
print(messages)