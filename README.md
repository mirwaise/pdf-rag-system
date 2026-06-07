# PDF RAG System

A Retrieval-Augmented Generation (RAG) application built using Python, ChromaDB, Groq, and PyPDF.

## Features

* Extract text from PDF files
* Clean and chunk document content
* Store chunks in ChromaDB
* Retrieve relevant information using semantic search
* Answer questions using Groq LLM

## Tech Stack

* Python
* PyPDF
* ChromaDB
* Groq API
* Llama 3

## How It Works

1. Extract text from PDF
2. Clean text using regex
3. Split text into chunks
4. Store chunks in ChromaDB
5. Retrieve relevant chunks based on user query
6. Send context to Groq LLM
7. Generate answer

## Example Questions

* What is my name?
* What internships have I completed?
* What are my skills?
* Summarize my profile.

## Future Improvements

* Better chunking strategy
* Streamlit UI
* Multiple PDF support
* Contract AI Extractor integration
