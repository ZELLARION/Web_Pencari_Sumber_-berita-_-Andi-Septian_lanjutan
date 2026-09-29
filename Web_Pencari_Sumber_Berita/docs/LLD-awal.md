# DRAF LLD AWAL (LOW-LEVEL DESIGN)

## Web Pencari Sumber Berita

### 1. Struktur Modul

```text
backend/
├── main.py
├── api/
│   └── search.py
├── services/
│   ├── ocr_service.py
│   ├── preprocessing_service.py
│   ├── keyword_service.py
│   ├── search_service.py
│   ├── scraper_service.py
│   └── similarity_service.py
├── scrapers/
│   ├── base.py
│   └── news_adapter.py
├── schemas/
│   └── search.py
└── models.py
```

### 2. Class/Service Responsibility

| Class/Service | Tanggung Jawab |
| --- | --- |
| `OCRService` | Menjalankan RapidOCR |
| `PreprocessingService` | Membersihkan teks |
| `KeywordService` | TF-IDF dan pemilihan keyword |
| `SearchService` | Membentuk dan menjalankan penelusuran |
| `ScraperService` | Mengambil artikel kandidat |
| `SimilarityService` | Vectorization dan Cosine Similarity |
| `RankingService` | Mengurutkan kandidat |
| `SearchRepository` | Menyimpan riwayat jika diperlukan |

### 3. OCRService

```python
class OCRService:
    def extract_text(self, image_path: str) -> str:
        ...
```

Input:
```text
image_path
```

Output:
```text
ocr_text
```

### 4. PreprocessingService

```python
class PreprocessingService:
    def clean(self, text: str) -> str:
        ...
```

Tahapan:
```text
lowercase
→ remove unnecessary symbols
→ normalize whitespace
→ tokenization
→ stopword handling
```

### 5. KeywordService

```python
class KeywordService:
    def extract_keywords(self, text: str, top_k: int = 10) -> list[str]:
        ...
```

TF-IDF digunakan untuk memberikan bobot terhadap kata dan memilih kata yang paling informatif.

### 6. SearchService

```python
class SearchService:
    def search(self, keywords: list[str]) -> list[str]:
        ...
```

Output:
```text
candidate_urls
```

### 7. ScraperService

```python
class ScraperService:
    def scrape(self, url: str) -> ArticleDocument:
        ...
```

`ArticleDocument`:

```python
{
    "source": "...",
    "title": "...",
    "url": "...",
    "published_at": "...",
    "content": "..."
}
```

Jurnal rujukan menggunakan elemen berita seperti media, judul, subjudul, URL, isi, tanggal, editor, jurnalis, dan lokasi sebagai hasil scraping. fileciteturn55file6

### 8. SimilarityService

```python
class SimilarityService:
    def calculate(self, query_text: str, candidate_text: str) -> float:
        ...
```

Konsep:

```text
query_text
      ↓
TF-IDF Vector
      ↓
Cosine Similarity
      ↑
TF-IDF Vector
      ↑
candidate_text
```

### 9. Ranking

```python
class RankingService:
    def rank(self, candidates):
        return sorted(
            candidates,
            key=lambda item: item["similarity"],
            reverse=True
        )
```

### 10. Pipeline Orchestrator

```python
class SourceSearchPipeline:
    def run(self, image_path):
        text = self.ocr.extract_text(image_path)
        clean_text = self.preprocess.clean(text)
        keywords = self.keyword.extract_keywords(clean_text)
        urls = self.search.search(keywords)
        articles = self.scraper.scrape_many(urls)
        results = self.similarity.compare(clean_text, articles)
        return self.ranking.rank(results)
```

### 11. Error Handling

Setiap service harus mengembalikan error yang dapat ditangani orchestrator sehingga kegagalan satu sumber tidak menghentikan seluruh pencarian.
