# 🎓 RAG-Based AI Assistance

An AI-powered Retrieval-Augmented Generation (RAG) system that converts lecture videos into a searchable knowledge base and enables users to obtain context-aware answers through natural-language queries.

---

## 🎯 Motivation

With the growing availability of recorded lectures and online learning resources, students often spend significant time searching through lengthy videos to locate a specific concept, explanation, or discussion. Traditional video platforms provide only basic navigation tools, making knowledge retrieval inefficient and time-consuming. This project was developed to bridge that gap by transforming educational content into an intelligent, searchable knowledge base that allows users to interact with their learning materials conversationally.

---

## 💡 Solution

The proposed system leverages Retrieval-Augmented Generation (RAG) to provide answers grounded in course content. Lecture videos are first converted into audio and transcribed into text. The transcripts are divided into meaningful chunks and transformed into vector embeddings for semantic search. When a user submits a query, the system retrieves the most relevant content and supplies it as context to a Large Language Model (LLM), enabling accurate and context-aware responses based on the uploaded material rather than relying solely on the model's pre-trained knowledge.

---

## ✨ Features

- Lecture video processing
- Automatic speech-to-text transcription
- Timestamp-aware content retrieval
- Semantic search using embeddings
- Context-aware question answering
- Retrieval-Augmented Generation (RAG)
- Local vector storage
- LLM-powered responses

---

## 🏗️ System Architecture

```text
Lecture Videos
      │
      ▼
Video to Audio Conversion
      │
      ▼
Whisper Transcription
      │
      ▼
Timestamped JSON Chunks
      │
      ▼
Embedding Generation
      │
      ▼
Vector Database
      │
      ▼
Similarity Search
      │
      ▼
Retrieved Context
      │
      ▼
Llama 3.2
      │
      ▼
Generated Answer
