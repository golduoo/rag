"""
Encoding Module.

This package contains vector encoding components for ingestion:
- Dense encoder (embedding vectors)
- Sparse encoder (BM25 term weights)
- Batch processor
"""

from src.ingestion.encoding.dense_encoder import DenseEncoder
from src.ingestion.encoding.sparse_encoder import SparseEncoder
from src.ingestion.encoding.batch_processor import BatchProcessor, BatchResult

__all__ = ["DenseEncoder", "SparseEncoder", "BatchProcessor", "BatchResult"]
