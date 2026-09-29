# USER FLOW

## Aktor

Aktor utama: **Pengguna**.

```mermaid
flowchart TD
    A[Pengguna membuka website]
    B[Upload citra berita]
    C{File valid?}
    D[RapidOCR]
    E{Teks ditemukan?}
    F[Preprocessing]
    G[TF-IDF]
    H[Keyword]
    I[Penelusuran berita]
    J[Scraping kandidat]
    K[Cosine Similarity]
    L[Ranking]
    M[Tampilkan sumber]
    N[Tampilkan error]

    A --> B
    B --> C
    C -- Tidak --> N
    C -- Ya --> D
    D --> E
    E -- Tidak --> N
    E -- Ya --> F
    F --> G
    G --> H
    H --> I
    I --> J
    J --> K
    K --> L
    L --> M
```

## Happy Path

1. Pengguna membuka website.
2. Pengguna mengunggah citra.
3. Sistem memvalidasi citra.
4. Sistem menjalankan RapidOCR.
5. Sistem membersihkan teks.
6. Sistem mengambil kata kunci.
7. Sistem menelusuri berita.
8. Sistem mengambil artikel kandidat.
9. Sistem menghitung similarity.
10. Sistem menampilkan ranking sumber.
