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

## Project Structure
rag_pipeline/
├── data/
│   ├── transcript.txt        # Merged transcript from OCR + audio
│   ├── book.txt              # Subject reference book used for retrieval
├── output/
│   └── final_summary.txt     # Final combined summary output
├── retriever.py              # FAISS-based retriever to fetch relevant context
├── summarizer.py             # Summarization logic using Hugging Face model
├── split_transcript.py       # Splits full transcript into 2-minute time chunks
├── summarize.py              # Main script to run the full RAG pipeline
├── faiss_store.index         # FAISS index storing vector embeddings (generated)
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation (this file)
└── .gitignore                # Specifies files/folders to be ignored by Git



