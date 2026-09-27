# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# import os

# #os.environ['HF_HOME'] = 'D:/huggingface_cache'     # this to give path of the local storage

# llm = HuggingFacePipeline.from_model_id(
#     #model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     model_id="Qwen/Qwen2.5-72B-Instruct",
#     task='text-generation',
#     pipeline_kwargs=dict(
#         temperature=0.5,
#         max_new_tokens=100
#     )
# )
# model = ChatHuggingFace(llm=llm)

# result = model.invoke("What is the capital of India")

# print(result.content)


import os
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# Optional: set custom cache path before loading
# os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    #model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100,
        "do_sample": True,  # Required when temperature > 0
    },
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")
print(result.content)