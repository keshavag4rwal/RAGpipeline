# from split_transcript import read_transcript, split_into_slots
# from retriever import FAISSRetriever
# from generator import SummaryGenerator

# def main():
#     # Step 1: Load and split transcript
#     print("🔹 Loading and splitting transcript...")
#     entries = read_transcript("data/transcript.txt")
#     print(f"🔍 Loaded {len(entries)} transcript entries")

#     slots = split_into_slots(entries, slot_minutes=2)

#     # Step 2: Initialize retriever
#     print("🔹 Setting up retriever...")
#     retriever = FAISSRetriever()
#     retriever.setup("data/book.txt")

#     # Step 3: Initialize generator
#     print("🔹 Loading summarization model...")
#     generator = SummaryGenerator()

#     # Step 4: Generate summaries
#     print("🔹 Generating summaries...")
#     final_summaries = []
#     prev_summary = ""

#     for idx, slot in enumerate(slots):
#         print(f"🧠 Summarizing slot {idx+1}/{len(slots)}...")
#         context_chunks = retriever.retrieve(slot, top_k=3)
#         context = " ".join(context_chunks)
#         summary = generator.generate_summary(slot, prev_summary, context)
#         final_summaries.append(summary)
#         prev_summary = summary  # Pass to next round

#     # Step 5: Save the final summary
#     print("✅ Saving summary to final_summary.txt...")
#     with open("final_summary.txt", "w", encoding="utf-8") as f:
#         for i, s in enumerate(final_summaries):
#             f.write(f"[Slot {i+1}]\n{s}\n\n")

#     print("🎉 Done! Final summary is saved in 'final_summary.txt'.")

# if __name__ == "__main__":
#     main()
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model and tokenizer globally (only once)
print("🔄 Loading summarization model...")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

def generate_summary(text):
    print(f"📨 Prompt length: {len(text)}")

    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)

    # Generate summary
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=150,
        num_beams=4,
        early_stopping=True
    )

    # Decode output
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    print(f"📤 Generated summary: {summary[:100]}...")  # Preview first 100 chars
    return summary
~