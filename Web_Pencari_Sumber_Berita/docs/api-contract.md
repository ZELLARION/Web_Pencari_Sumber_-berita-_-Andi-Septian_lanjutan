# API CONTRACT

## POST `/api/search-source`

### Request

```http
POST /api/search-source
Content-Type: multipart/form-data
```

Field:

| Field | Type | Required |
| --- | --- | --- |
| `image` | file | Yes |

### Response 200

```json
{
  "ocr_text": "contoh teks berita",
  "keywords": ["jombang", "berita", "pemerintah"],
  "results": [
    {
      "source": "Portal Berita",
      "title": "Judul Artikel",
      "url": "https://example.com/article",
      "published_at": "2026-01-01",
      "similarity": 0.87
    }
  ]
}
```

### Error

```json
{
  "error": {
    "code": "OCR_NO_TEXT",
    "message": "Teks tidak berhasil ditemukan pada citra."
  }
}
```

### Kode Error

| Code | Makna |
| --- | --- |
| `INVALID_FILE` | File bukan citra yang didukung |
| `OCR_NO_TEXT` | Tidak ada teks yang dapat digunakan |
| `SEARCH_FAILED` | Penelusuran gagal |
| `SCRAPE_FAILED` | Artikel kandidat gagal diambil |
| `INTERNAL_ERROR` | Kesalahan internal |
