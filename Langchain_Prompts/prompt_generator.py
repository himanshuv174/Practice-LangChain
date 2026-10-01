# This will create a prompt template and save it in a json format with name "template.json", SO that it can be used again and again.
import json
from langchain_core.load import dumpd, dumps

from langchain_core.prompts import PromptTemplate

# template
template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input','length_input'],
validate_template=True
)

#template.save('template.json')   #not working in new version

# Both two methods dumps and dumpd gives the same output

# Serialize the prompt template to a JSON string and write to file using dumps
# with open("template2.json", "w", encoding="utf-8") as f:
#     f.write(dumps(template, pretty=True))

# Save in a file using the json library and dumpd
with open("template.json", "w", encoding="utf-8") as f:
    json.dump(dumpd(template), f, indent=2) 