from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class SummaryGenerator:
    def __init__(self, model_name='google/flan-t5-base', device=None):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def generate_summary(self, slot_text, previous_summary, context, max_tokens=256):
        """Generate summary from slot + previous summary + book context."""
        prompt = f"""
        Using the following book context and previously generated summary, write a concise summary for the new transcript segment.

        [Book Context]: {context}

        [Previous Summary]: {previous_summary}

        [New Transcript Slot]: {slot_text}

        [Summary]:
        """
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, padding=True, max_length=1024)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        outputs = self.model.generate(**inputs, max_new_tokens=max_tokens)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
