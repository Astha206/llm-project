
from google import genai
from dotenv import load_dotenv
import os 

load_dotenv()

MAX_CHARS = 10000

def load_document(file_path):
    with open(file_path,"r",encoding="utf-8") as file:
     document = file.read()

    if len(document) > MAX_CHARS:
        raise ValueError(
            f"Document is too large. Maximum allowed size is {MAX_CHARS} characters."
        )

    return document 


def ask_question(client,document,question):
      
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

    return response.text


def main():
    document = load_document("knowledge.txt")

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    while(True):
        question = input("Ask your question:")

        if question =="quit":
         break
        answer = ask_question(client,document,question)

        print(answer)


if __name__ == "__main__":
    main()