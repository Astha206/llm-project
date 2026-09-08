from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

question = input("Ask me something: ")

response = client.models.generate_content(
    model = "gemini-3.7-flash",
    contents =question
)

print(response.text)