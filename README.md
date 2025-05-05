# YouTube Lecture Summarizer using RAG (Retrieval-Augmented Generation)

This project summarizes educational YouTube videos by combining OCR, audio transcription, and retrieval-augmented generation (RAG) with a subject textbook as a knowledge base.

---

## Features

- **OCR + Speech-to-Text**: Extracts both visual and spoken text from video.
- **Knowledge-Guided Summarization**: Uses textbook content to improve factual consistency.
- **FAISS Retriever**: Retrieves relevant knowledge chunks using similarity search.
- ✂**Time-based Splitting**: Processes video transcripts in 2-minute chunks for contextual accuracy.
- **Final Output**: A comprehensive, section-wise summary in `output/final_summary.txt`.

---

