# Document Q&A with Gemini API

*Project 1 of an ongoing GenAI learning series.*

## Why This Project?

A small document question-answering tool built with Python and the Gemini API.

This is a learning project focused on understanding **LLM API fundamentals and document grounding** directly through the API, before introducing higher-level frameworks. Future projects will build on this with RAG and agent frameworks.

## What It Does

1. Reads a document from `knowledge.txt`
2. Takes a question from the user
3. Sends the document + question to Gemini, instructed to answer only from the document
4. Returns the answer (or says the document doesn't contain it)

```text
knowledge.txt + user question → Gemini API → answer
Concepts Learned
Making LLM API calls
System instructions and prompt construction
Providing external context to an LLM (grounding)
Context windows, tokens vs. characters
Structuring Python code with functions
Environment variables / API keys
Basic input-size validation
Setup
python -m venv .venv
.\.venv\Scripts\Activate.ps1        # Windows
pip install google-genai python-dotenv

Add a .env file with:

GEMINI_API_KEY=your_api_key_here

Don't commit your .env file.

Place your document in knowledge.txt and run:

python document_qa.py

Type quit to exit.

Current Limitation

The entire document is included in every prompt, which doesn't scale to large documents. The app enforces its own MAX_CHARS = 10000 limit — this is our own safety limit, not Gemini's actual context limit.

A more scalable approach would retrieve only the relevant parts of a document instead of sending all of it — that's what a future RAG-based project will explore.
