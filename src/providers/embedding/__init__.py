"""
Embedding Module.

This package contains embedding service abstractions and implementations:
- Base embedding class
- Embedding factory
- Provider implementations (OpenAI, Azure, Ollama)
"""

from src.providers.embedding.azure_embedding import AzureEmbedding
from src.providers.embedding.base_embedding import BaseEmbedding
from src.providers.embedding.embedding_factory import EmbeddingFactory
from src.providers.embedding.ollama_embedding import OllamaEmbedding
from src.providers.embedding.openai_embedding import OpenAIEmbedding

__all__ = [
    "BaseEmbedding",
    "EmbeddingFactory",
    "OpenAIEmbedding",
    "AzureEmbedding",
    "OllamaEmbedding",
]
