from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

llm = ChatOllama(
    model="llama3.2-lowmem:latest",
    temperature=0.7
)
chat_history = [
    SystemMessage(content="You are a helpful, witty, and intelligent AI assistant like ChatGPT or Gemini.")
]
print("--- AI Q&A Bot Ready (Type 'exit' to quit) ---\n")

while True:
    prompt = input("You: ").strip()

    if not prompt:
        continue

    if prompt.lower() in ["exit", "quit", "q"]:
        print("AI: Goodbye!")
        break
    print("AI: ", end="", flush=True)
    chat_history.append(HumanMessage(content=prompt))

    response = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(response.content)