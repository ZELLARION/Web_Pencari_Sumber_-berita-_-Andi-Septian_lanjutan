from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ArticleDocument:
    source: str
    title: str
    url: str
    content: str
    published_at: Optional[datetime] = None


@dataclass
class SearchResult:
    source: str
    title: str
    url: str
    similarity: float
    published_at: Optional[datetime] = None


@dataclass
class SearchResponse:
    ocr_text: str
    keywords: list[str]
    results: list[SearchResult]
