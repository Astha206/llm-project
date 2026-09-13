# Document Q&A with Gemini API

A small document question-answering tool built with Python and the Gemini API.

This project was created as a **learning project to understand the fundamentals of Generative AI and LLM APIs**. It focuses on making raw API calls and understanding how documents can be provided as context to an LLM, without using frameworks such as LangChain or RAG.

## What This Project Does

The program:

1. Reads a text document from `knowledge.txt`
2. Loads the document into Python
3. Takes questions from the user
4. Sends the document and question to Gemini
5. Instructs Gemini to answer using only the provided document
6. Returns the answer to the user

If the answer cannot be found in the document, the model is instructed to say that the document does not contain the answer.

## How It Works

```text
knowledge.txt
      ↓
load_document()
      ↓
Document text
      ↓
User question
      ↓
Document + Question
      ↓
Gemini API
      ↓
Answer

The document is included directly in the prompt as context. This is a simple approach for understanding how LLM grounding works.

Concepts Learned

This project helped explore the following GenAI fundamentals:

Making API calls to an LLM
System instructions
Prompt construction
Providing external context to an LLM
Document grounding
Context windows
Tokens vs. characters
Structuring an LLM application using Python functions
Environment variables and API keys
Basic input-size validation
Technologies Used
Python
Gemini API
google-genai
python-dotenv
Project Structure
document-qa/
│
├── document_qa.py
├── knowledge.txt
├── .env
├── .gitignore
└── README.md
Setup
1. Create and activate a virtual environment
python -m venv .venv

On Windows PowerShell:

.\.venv\Scripts\Activate.ps1
2. Install dependencies
pip install google-genai python-dotenv
3. Add your API key

Create a .env file:

GEMINI_API_KEY=your_api_key_here

Do not commit your .env file to GitHub.

4. Add your document

Place the text you want to query inside:

knowledge.txt
5. Run the application
python document_qa.py

You can then ask questions about the document.

Type:

quit

to exit.

Current Limitation

The entire document is included in the prompt for every question.

This works well for small documents, but it does not scale efficiently to very large documents because LLMs have finite context windows.

The project therefore includes an application-level document size check:

MAX_CHARS = 10000

This is our own safety limit, not the actual context limit of the Gemini model.

A more scalable approach would retrieve only the relevant parts of a large document instead of sending the entire document every time. This project intentionally does not implement that yet.

Why This Project?

This project is part of my learning process for Generative AI and Large Language Models.

The goal was to first understand the fundamentals by working directly with the Gemini API before introducing higher-level frameworks and techniques.

Future projects will build on these concepts and explore more scalable approaches such as RAG and LLM frameworks.
