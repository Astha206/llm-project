
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

while(True):
  question = input("Ask me something: ")

  if question == "quit":
     break

  
  response = client.models.generate_content(
    model = "gemini-3.7-flash",
    contents =question,
    config = genai.types.GenerateContentConfig(
        system_instruction="You are a concise technical tutor.",
        
    )

    )



  print(response.text)