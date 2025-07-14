import re

def clean_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()

def chunk_text(text: str, max_chars: int = 15000):
    return [text[i : i + max_chars] for i in range(0, len(text), max_chars)]
