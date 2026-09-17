\# AI/ML Internship



A 6-week AI/ML project focused on building a Retrieval-Augmented Generation (RAG) system for knowledge extraction from real-world text data.



\## Project Overview



The project will develop an end-to-end RAG pipeline that includes:



\* Real-world document ingestion and preprocessing

\* Text chunking and embedding

\* Vector storage and semantic retrieval using ChromaDB

\* Grounded response generation using an LLM

\* Topic modeling and sentiment analysis

\* RAG evaluation and hallucination detection

\* API or CLI-based access to the system



\## Week 1 — Environment, Data Ingestion \& Preprocessing



\### Current Progress



\* Initialized the Git repository.

\* Created an isolated Python 3.12 virtual environment using `uv`.

\* Added a `.gitignore` to exclude virtual environment, secrets, and dataset files.

\* Installed the initial AI/ML and NLP dependencies.

\* Created an environment verification script.

\* Verified imports for pandas, sentence-transformers, ChromaDB, spaCy, and PyTorch.

\* Verified that PyTorch is running with CPU support.

\* Confirmed that CUDA is not available on the current machine.



\### Project Structure



```text

AI-ML-Internship/

├── data/

│   ├── raw/

│   └── processed/

├── scripts/

│   └── verify\_env.py

├── src/

├── tests/

├── .gitignore

├── requirements.txt

└── README.md

```



\### Environment



\* Python: 3.12.13

\* PyTorch: 2.14.0+cpu

\* Package manager: uv

\* Operating system: Windows



\### Installed Core Dependencies



\* pandas

\* sentence-transformers

\* chromadb

\* spaCy

\* PyTorch



The complete locked dependency list is available in `requirements.txt`.



\### Environment Verification



Run:



```bash

python scripts/verify\_env.py

```



The verification script checks the Python version, CUDA availability, and required library imports.



\### CUDA Status



The current development machine has an Intel UHD Graphics GPU and does not provide NVIDIA CUDA support. PyTorch therefore runs using CPU.



\### Setup



Create the virtual environment:



```bash

uv venv --python 3.12

```



Activate it on Windows:



```bash

.venv\\Scripts\\activate

```



Install dependencies:



```bash

uv pip install -r requirements.txt

```



\### Data Policy



Raw and processed datasets are excluded from Git tracking because they may contain large files. Dataset files are stored locally under:



```text

data/raw/

data/processed/

```



\## Upcoming Work



\* Acquire a real-world text dataset containing 5,000+ documents.

\* Implement modular text cleaning and language filtering.

\* Build the preprocessing pipeline.

\* Add unit tests for preprocessing.

\* Generate and validate the cleaned corpus.



