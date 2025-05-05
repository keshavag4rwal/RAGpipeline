import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

class FAISSRetriever:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.text_chunks = []

    def load_book(self, file_path, chunk_size=100):
        """Load and split book into chunks of `chunk_size` words."""
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        words = text.split()
        self.text_chunks = [
            " ".join(words[i:i+chunk_size])
            for i in range(0, len(words), chunk_size)
        ]

    def build_index(self):
        """Embed text chunks and build FAISS index."""
        embeddings = self.model.encode(self.text_chunks, show_progress_bar=True)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings).astype("float32"))

    def retrieve(self, query, top_k=3):
        """Retrieve top-k relevant chunks for a given query."""
        query_embedding = self.model.encode([query])
        D, I = self.index.search(np.array(query_embedding).astype("float32"), top_k)
        return [self.text_chunks[i] for i in I[0]]

    def setup(self, book_path):
        """Convenience method to load and index the book."""
        if not os.path.exists(book_path):
            raise FileNotFoundError(f"Book file not found: {book_path}")
        self.load_book(book_path)
        self.build_index()
