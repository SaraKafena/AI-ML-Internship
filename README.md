# RAG-Powered Knowledge Extraction System

An AI/ML project focused on building a Retrieval-Augmented Generation (RAG) system for extracting and retrieving knowledge from large-scale real-world text data.

The project combines document ingestion, text preprocessing, semantic search, vector databases, and Large Language Models (LLMs) to build a grounded knowledge extraction pipeline.

## Project Overview

The system is designed as an end-to-end pipeline that processes documents from multiple sources and prepares them for semantic retrieval and RAG-based question answering.

The planned pipeline includes:

* Real-world document ingestion
* Text cleaning and preprocessing
* Document chunking
* Text embeddings
* Vector storage using ChromaDB
* Semantic retrieval
* Context-grounded LLM responses
* Topic modeling
* Sentiment analysis
* Retrieval and response evaluation
* Hallucination detection
* CLI or API-based access

## Architecture

The project follows a modular pipeline:

```text
Data Sources
     │
     ▼
Document Ingestion
     │
     ▼
Text Preprocessing
     │
     ▼
Cleaned Corpus
     │
     ▼
Chunking
     │
     ▼
Embeddings
     │
     ▼
ChromaDB
     │
     ▼
Semantic Retrieval
     │
     ▼
Retrieved Context
     │
     ▼
LLM
     │
     ▼
Grounded Response
```

Additional NLP analysis components are planned for topic modeling, sentiment analysis, and system evaluation.

## Data Sources

The current dataset is collected from three real-world text sources:

* **ArXiv** — scientific and research documents
* **Reddit** — user-generated discussions and opinions
* **Wikipedia** — general knowledge articles

The project targets a corpus of **5,000+ documents**.

Raw and processed datasets are stored locally and are excluded from Git tracking.

## Data Ingestion

Document ingestion is implemented in:

```text
src/ingestion.py
```

The ingestion component handles the collection and preparation of documents from the supported data sources before they enter the preprocessing pipeline.

The current raw datasets are stored locally as JSONL files:

```text
data/raw/
├── arxiv.jsonl
├── reddit.jsonl
└── wikipedia.jsonl
```

## Preprocessing

The preprocessing pipeline is implemented in:

```text
src/preprocessing.py
```

Current preprocessing operations include:

* HTML removal
* Unicode normalization
* Whitespace cleanup
* Language filtering

The processed corpus is generated as:

```text
data/processed/clean_corpus.jsonl
```

The preprocessing pipeline is designed as a modular component so additional cleaning and validation steps can be added as the project evolves.

## Project Structure

```text
AI-ML-Internship/
│
├── data/
│   ├── raw/
│   │   ├── arxiv.jsonl
│   │   ├── reddit.jsonl
│   │   └── wikipedia.jsonl
│   │
│   └── processed/
│       └── clean_corpus.jsonl
│
├── scripts/
│   └── verify_env.py
│
├── src/
│   ├── ingestion.py
│   ├── preprocessing.py
│   └── __init__.py
│
├── tests/
│   └── test_preprocessing.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

> Dataset files under `data/` are intentionally excluded from Git tracking.

## Environment & Dependencies

The project currently uses:

* **Python 3.12.13**
* **PyTorch**
* **pandas**
* **sentence-transformers**
* **ChromaDB**
* **spaCy**
* **uv** for environment and package management

The complete dependency list is available in:

```text
requirements.txt
```

The current development environment uses CPU-based PyTorch because CUDA is not available on the development machine.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/SaraKafena/AI-ML-Internship.git
cd AI-ML-Internship
```

### 2. Create the virtual environment

```bash
uv venv --python 3.12
```

### 3. Activate the environment on Windows

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
uv pip install -r requirements.txt
```

## Environment Verification

The repository includes an environment verification script:

```text
scripts/verify_env.py
```

Run it with:

```bash
python scripts/verify_env.py
```

The script verifies the Python environment, checks CUDA availability, and confirms that the required AI/ML and NLP libraries can be imported successfully.

## Testing

Preprocessing functionality is tested using `pytest`.

Run the test suite with:

```bash
pytest
```

Current tests are located in:

```text
tests/test_preprocessing.py
```

## Data Policy

Raw and processed datasets are excluded from Git tracking because they may contain large amounts of data.

Local datasets should be stored under:

```text
data/raw/
data/processed/
```

These directories are excluded through `.gitignore`.

## Current Status

### Implemented

* Project repository and development environment
* Python 3.12 environment using `uv`
* Dependency configuration
* Environment verification
* Data ingestion module
* Raw document collection from ArXiv, Reddit, and Wikipedia
* Text preprocessing pipeline
* Cleaned JSONL corpus
* Preprocessing tests
* Data exclusion through `.gitignore`

### In Development

The next stages of the system focus on:

* Document chunking
* Embedding generation
* ChromaDB vector storage
* Semantic retrieval
* LLM integration
* RAG response generation
* Topic modeling
* Sentiment analysis
* Retrieval and generation evaluation
* Hallucination detection
* CLI or API interface

## License

This project is developed as an AI/ML engineering portfolio project.
