with open("knowledge.txt","r",encoding="utf-8") as file:
    document = file.read()

from google import genai
from dotenv import load_dotenv
import os 

load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


while(True):
    question = input("Ask a question about the document:")

    if question == "quit":
        break
    
    response = client.models.generate_content(
    model= "gemini-3.6-flash",
    contents=f"""
You are answering questions about the provided document.

DOCUMENT:
{document}

QUESTION:
{question}

Answer the question using only the information provided in the document.
If the answer is not present in the document, say that the document does not contain the answer.
"""
)

    print(response.text)

