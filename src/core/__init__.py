"""
Core Layer - Shared types and configuration.

This package contains the fundamental building blocks shared across all layers:
- Configuration management (settings.py)
- Core data types (types.py) - shared contracts for all pipeline stages
"""

from src.core.types import Document, Chunk, ChunkRecord, Metadata, Vector, SparseVector

__all__ = [
    "Document",
    "Chunk", 
    "ChunkRecord",
    "Metadata",
    "Vector",
    "SparseVector"
]
