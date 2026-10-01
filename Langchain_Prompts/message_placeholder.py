# Creating a Chat prompt using the dynamic prompting using the Message place holder.
#It will take the system, human and the previous Chats from chat_history.txt and add it will the new user request.
#From this the new message or prompts in the Chat will have all the context of the previous conversations.

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template

#Creating a Chat Template with system, human and a Message Placeholder which keeps the context of previous Chats stored.
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# load chat history from the files OR May be DB.
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# creating the prompt keeping the previous history in account and adding new query.
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)