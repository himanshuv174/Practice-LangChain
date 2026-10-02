# We are giving a reviews to our Chat Model and asking him to give us a summary and the sentiment of that review in a structured format using a TypedDict Dictionary.

import os
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
# from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen2.5-72B-Instruct",  # Choose any supported HF model
    task = 'text-generation',
    huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)
# model = ChatOpenAI()

model = ChatHuggingFace(llm = llm)

# schema of the output data format
# Giving the annotated of the variable with a small description.
# Optional defines for the optional variable in the output.
# Literals are used to give few values, it can return. It will not return the value that are not present in Literals.

class Review(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["postive", "negative","neutral"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]
    

structured_model = model.with_structured_output(Review)  #giving the schema of the output in the form of a class to with_structured_output function.

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Anshu
""")

print(result['name'])
# print(result)
#print(result['summary'])


######################################################################
# Output looks like 

# {'name': 'Anshu', 
#  'summary': 'A powerful and feature-rich device with some notable drawbacks.', 
#  'sentiment': 'postive', 
#  'key_themes': ['Processor Performance', 'Battery Life', 'Camera Quality', 'S-Pen Integration', 'Size and Weight', 'Bloatware', 'Price'], 
#  'pros': ['Insanely powerful processor (great for gaming and productivity)', 'Stunning 200MP camera with incredible zoom capabilities', 'Long battery life with fast charging', 'S-Pen support is unique and useful'], 
#  'cons': ['Weight and size make it uncomfortable for one-handed use', 'One UI comes with unnecessary bloatware', 'High price tag']}