from pathlib import Path
import json
import re
import unicodedata
from html import unescape

from langdetect import DetectorFactory, detect, LangDetectException


DetectorFactory.seed = 0

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
OUTPUT_FILE = PROCESSED_DIR / "clean_corpus.jsonl"


def strip_html(text):
    """Remove HTML tags and decode HTML entities."""
    text = re.sub(r"<[^>]+>", " ", text)
    return unescape(text)


def normalize_unicode(text):
    """Normalize Unicode characters."""
    return unicodedata.normalize("NFKC", text)


def clean_whitespace(text):
    """Normalize spaces, tabs, and line breaks."""
    return re.sub(r"\s+", " ", text).strip()


def clean_text(text):
    """Apply all text-cleaning steps."""
    if not text:
        return ""

    text = strip_html(text)
    text = normalize_unicode(text)
    text = clean_whitespace(text)

    return text


def is_english(text):
    """Check whether the text is English."""
    if len(text.strip()) < 20:
        return False

    try:
        return detect(text) == "en"
    except LangDetectException:
        return False


def load_raw_documents():
    """Load documents from all raw JSONL files."""
    documents = []

    for file_path in sorted(RAW_DIR.glob("*.jsonl")):
        with file_path.open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    documents.append(json.loads(line))

    return documents


def preprocess_documents(documents):
    """Clean, filter, and deduplicate documents."""
    processed = []
    seen_texts = set()

    for document in documents:
        original_text = document.get("text", "")
        cleaned = clean_text(original_text)

        if not cleaned:
            continue

        if not is_english(cleaned):
            continue

        if cleaned in seen_texts:
            continue

        seen_texts.add(cleaned)

        processed.append({
            "id": document.get("id", ""),
            "source": document.get("source", ""),
            "title": clean_text(document.get("title", "")),
            "text": cleaned,
            "url": document.get("url", ""),
        })

    return processed


def save_documents(documents):
    """Save processed documents as JSONL."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        for document in documents:
            f.write(json.dumps(document, ensure_ascii=False) + "\n")


def main():
    print("=== Text Preprocessing ===")

    print("Loading raw documents...")
    documents = load_raw_documents()
    print(f"Raw documents: {len(documents)}")

    print("Cleaning and filtering...")
    processed = preprocess_documents(documents)

    save_documents(processed)

    print(f"✓ Clean documents: {len(processed)}")
    print(f"✓ Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()