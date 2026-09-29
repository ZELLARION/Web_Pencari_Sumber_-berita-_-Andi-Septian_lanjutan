# Web Pencari Sumber Berita

## Penerapan RapidOCR OCR dan Cosine Similarity untuk Penelusuran Sumber Berita Berbasis Web melalui Ekstraksi Teks Citra

Project ini dirancang sebagai sistem berbasis website untuk membantu pengguna menelusuri sumber berita berdasarkan teks yang terdapat pada citra. Sistem menerima citra berita/screenshot, melakukan ekstraksi teks menggunakan RapidOCR, menentukan kata kunci menggunakan TF-IDF, melakukan penelusuran pada sumber berita online, kemudian membandingkan teks OCR dengan artikel kandidat menggunakan Cosine Similarity.

### Referensi utama

Hafiz, Y. A., & Sudarmilah, E. (2023). **Implementasi Web Scraping pada Portal Berita Online**. INISIASI, 12(1). Referensi ini digunakan terutama sebagai acuan proses web scraping: penentuan situs objek, eksplorasi struktur HTML, identifikasi elemen berita, menjalankan scraping, dan menghasilkan data terstruktur/CSV. Jurnal juga menjelaskan bahwa web scraping dapat membantu pengumpulan data berita secara otomatis dan mendukung analisis tren maupun sentimen.

### Alur utama

```text
Citra Berita
    ↓
RapidOCR
    ↓
Teks OCR
    ↓
Preprocessing
    ↓
TF-IDF
    ↓
Kata Kunci
    ↓
Penelusuran Sumber Berita
    ↓
Web Scraping Artikel Kandidat
    ↓
TF-IDF + Cosine Similarity
    ↓
Ranking Kemiripan
    ↓
Sumber Berita Paling Relevan
```
