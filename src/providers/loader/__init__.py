"""
Loader Module.

This package contains document loader components:
- Base loader class
- PDF loader
- File integrity checker
"""

from src.providers.loader.base_loader import BaseLoader
from src.providers.loader.pdf_loader import PdfLoader
from src.providers.loader.file_integrity import FileIntegrityChecker, SQLiteIntegrityChecker

__all__ = [
    "BaseLoader",
    "PdfLoader",
    "FileIntegrityChecker",
    "SQLiteIntegrityChecker",
]
