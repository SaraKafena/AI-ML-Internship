import sys

import pandas as pd
import torch
import sentence_transformers
import chromadb
import spacy


def check_python_version():
    """Check that the project is using Python 3.12."""
    major, minor = sys.version_info[:2]

    assert (major, minor) == (3, 12), (
        f"Expected Python 3.12, but found Python {major}.{minor}"
    )

    print(f"✓ Python {major}.{minor} detected")


def check_cuda():
    """Check CUDA availability through PyTorch."""
    if torch.cuda.is_available():
        print(f"✓ CUDA available: {torch.cuda.get_device_name(0)}")
    else:
        print("⚠ CUDA not available — using CPU")


def check_imports():
    """Verify that the required ML/NLP libraries can be imported."""
    print("✓ pandas imported")
    print("✓ sentence-transformers imported")
    print("✓ chromadb imported")
    print("✓ spaCy imported")
    print("✓ PyTorch imported")


def main():
    print("=== AI/ML Internship Environment Verification ===")

    check_python_version()
    check_cuda()
    check_imports()

    print("\nEnvironment verification completed successfully.")


if __name__ == "__main__":
    main()