from pathlib import Path
import json

from datasets import load_dataset


RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)


def save_jsonl(records, output_file):
    """Save records as JSON Lines."""
    with output_file.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def collect_wikipedia(limit=2000):
    """Collect Wikipedia articles."""
    print("Collecting Wikipedia...")

    dataset = load_dataset(
        "wikimedia/wikipedia",
        "20231101.en",
        split="train",
        streaming=True,
    )

    records = []

    for item in dataset:
        if not item.get("text"):
            continue

        records.append({
            "id": f"wikipedia_{item['id']}",
            "source": "wikipedia",
            "title": item.get("title", ""),
            "text": item["text"],
            "url": item.get("url", ""),
        })

        if len(records) >= limit:
            break

    save_jsonl(records, RAW_DIR / "wikipedia.jsonl")
    print(f"✓ Wikipedia: {len(records)} documents")


def collect_arxiv(limit=2000):
    """Collect arXiv abstracts."""
    print("Collecting ArXiv...")

    dataset = load_dataset(
        "common-pile/arxiv_abstracts",
        split="train",
        streaming=True,
    )

    records = []

    for item in dataset:
        if not item.get("text"):
            continue

        metadata = item.get("metadata") or {}

        records.append({
            "id": f"arxiv_{item['id']}",
            "source": "arxiv",
            "title": "",
            "text": item["text"],
            "url": metadata.get("url", ""),
        })

        if len(records) >= limit:
            break

    save_jsonl(records, RAW_DIR / "arxiv.jsonl")
    print(f"✓ ArXiv: {len(records)} documents")


def collect_reddit(limit=2000):
    """Collect Reddit posts."""
    print("Collecting Reddit...")

    dataset = load_dataset(
        "sentence-transformers/reddit",
        split="train",
        streaming=True,
    )

    records = []

    for item in dataset:
        title = item.get("title", "")
        body = item.get("body", "")

        text = f"{title}\n\n{body}".strip()

        if not text:
            continue

        records.append({
            "id": f"reddit_{len(records)}",
            "source": "reddit",
            "title": title,
            "text": text,
            "url": "",
        })

        if len(records) >= limit:
            break

    save_jsonl(records, RAW_DIR / "reddit.jsonl")
    print(f"✓ Reddit: {len(records)} documents")


def main():
    collect_wikipedia(limit=2000)
    collect_arxiv(limit=2000)
    collect_reddit(limit=2000)

    print("\n=== Data ingestion completed ===")
    print("Total documents: 6000")


if __name__ == "__main__":
    main()