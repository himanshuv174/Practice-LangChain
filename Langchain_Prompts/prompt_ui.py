# A Steamlit Application with the AI Summarization of the given Documents. 
# # It lives in a Local Host, I gives the response in the user given directions/Prompts/Language/Nature in the frontend Streamlit Application.
# # Select the dropdown and click on the Summarize button to get the Output.

import os
import streamlit as st
from dotenv import load_dotenv
#from langchain_core.prompts import load_prompt
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import json
from langchain_core.load import load, loads

load_dotenv()

# Define the remote HF Inference model
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",  # Choose any supported HF model
    task="text-generation",
    max_new_tokens=512,
    temperature=0.7,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

model = ChatHuggingFace(llm=llm)


st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


# Creating a Prompt Template, So that it will give all the outputs in a defined format.
#template = load_prompt('template.json')     

# Both using load and Loads gives the same output

# Using Python's built-in json module with load
with open("template.json", "r", encoding="utf-8") as f:
    template = load(json.load(f))

# Read the JSON file contents as a string and deserialize with loads.
# with open("template.json", "r", encoding="utf-8") as f:
#     template = loads(f.read())



if st.button('Summarize'):
    chain = template | model     #Creating a chain for template and model, Otherwise we need to invoke the template and model seperately
    result = chain.invoke({      # it will invoke the chain with Prompt template and the User input, and it will summarize the result in the form of the template prompt and give response.
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)


    