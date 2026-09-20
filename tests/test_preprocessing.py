import json
from pathlib import Path

from src.preprocessing import (
    clean_text,
    is_english,
    strip_html,
    normalize_unicode,
    clean_whitespace,
)


def test_strip_html():
    text = "<p>Hello <b>world</b></p>"
    result = strip_html(text)

    assert "<p>" not in result
    assert "<b>" not in result
    assert "Hello" in result
    assert "world" in result


def test_normalize_unicode():
    text = "ＡＩ"
    result = normalize_unicode(text)

    assert result == "AI"


def test_clean_whitespace():
    text = "Hello    world\n\nthis is a test"
    result = clean_whitespace(text)

    assert result == "Hello world this is a test"


def test_clean_text():
    text = "<p>Hello    world!</p>"
    result = clean_text(text)

    assert result == "Hello world!"


def test_is_english():
    assert is_english("This is a simple English sentence for testing.")
    assert not is_english("مرحبا كيف حالك")


def test_output_file_exists():
    output_file = Path("data/processed/clean_corpus.jsonl")

    assert output_file.exists()

    with output_file.open("r", encoding="utf-8") as f:
        documents = [json.loads(line) for line in f if line.strip()]

    assert len(documents) >= 5000


def test_output_schema():
    output_file = Path("data/processed/clean_corpus.jsonl")

    with output_file.open("r", encoding="utf-8") as f:
        document = json.loads(next(line for line in f if line.strip()))

    required_fields = {"id", "source", "title", "text", "url"}

    assert required_fields.issubset(document.keys())
    assert document["text"]