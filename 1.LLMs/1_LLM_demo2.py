import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# 1. Initialize the Gemini chat model
# You can pass the key explicitly via google_api_key=... or rely on GOOGLE_API_KEY env var
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# 2. Define a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior data engineer helping optimize batch and streaming data pipelines."),
    ("human", "{question}")
])

# 3. Build the pipeline (LCEL)
chain = prompt | llm | StrOutputParser()

# 4. Invoke
response = chain.invoke({
    "question": "What are key considerations when tuning shuffle partitions in PySpark for skewed joins?"
})

print(response)