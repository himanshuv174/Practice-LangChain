import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    # Supported serverless chat model:
    #repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    #repo_id="meta-llama/Llama-3.2-1B-Instruct",
    #repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=256,
    temperature=0.7,
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")
print(result.content)