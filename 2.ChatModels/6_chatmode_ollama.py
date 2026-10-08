# Steps : Make sure Ollama and the library are installed
# Download & install Ollama from ollama.com (if not already done).
# Pull a model that supports structured outputs / tool calling (e.g., llama3.2):

# Bash
# ollama run llama3.2

# (Once it finishes downloading, you can type /bye to exit the chat; Ollama keeps running in the background).
# Install the LangChain Ollama integration package:

# Bash
# pip install langchain-ollama

from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.2", temperature=0)

result = model.invoke("What is the capital of India")
print(result.content)