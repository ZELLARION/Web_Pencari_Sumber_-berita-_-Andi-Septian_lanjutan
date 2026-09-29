# ERD

## Entitas

```mermaid
erDiagram
    SEARCH_SESSION ||--o{ SEARCH_RESULT : contains

    SEARCH_SESSION {
        int id PK
        datetime created_at
        string original_filename
        text ocr_text
        text keywords
    }

    SEARCH_RESULT {
        int id PK
        int search_id FK
        string source
        string title
        string url
        datetime published_at
        float similarity
    }
```

## Penjelasan

### SEARCH_SESSION

Menyimpan informasi satu proses pencarian.

### SEARCH_RESULT

Menyimpan kandidat sumber yang dihasilkan dari satu proses pencarian.

**Catatan:** database bersifat opsional untuk prototype apabila riwayat pencarian tidak diperlukan.
