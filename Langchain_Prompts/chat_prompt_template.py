#Example of Chat Prompt Template. Instead of using the SystemMessage and HumanMessage, we are using the Tuples of system and human.
#This is used to give the multiple Chat template.

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)