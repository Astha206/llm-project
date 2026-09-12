
from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


while True:
  question = input("\nAsk me something (or type 'quit' to exit): ")

  if question.strip().lower() == "quit":
    break
  response = client.models.generate_content(
    model = "gemini-3.6-flash",
    contents = question,
    config = genai.types.GenerateContentConfig(
        system_instruction="You are a concise technical tutor.",
        response_mime_type= "application/json",
        response_schema={
                "type": "OBJECT",
                "properties": {
                    "explanation": {
                        "type": "OBJECT",
                        "properties": {
                            "definition": {"type": "STRING"},
                            "example": {"type": "STRING"}
                        },
                        "required": ["definition", "example"]
                    },
                    "use_cases": {
                        "type": "ARRAY",
                        "items": {"type": "STRING"}
                    }
                },
                "required": ["explanation", "use_cases"]
            }

        
    )

    )

  data = json.loads(response.text)
  
  print("\n" + "=" * 50)
  print("DEFINITION:")
  print(data["explanation"]["definition"])
  
  print("\nEXAMPLE:")
  print(data["explanation"]["example"])
  
  print("\nUSE CASES:")
  for use_case in data["use_cases"]:
    print("• ", use_case)
  print("=" * 50)
 
