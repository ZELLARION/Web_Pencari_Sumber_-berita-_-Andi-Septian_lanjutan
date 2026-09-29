# DRAF PRD (PRODUCT REQUIREMENTS DOCUMENT)

## Web Pencari Sumber Berita Berbasis Ekstraksi Teks Citra

### 1. Ringkasan Eksekutif

Web Pencari Sumber Berita adalah produk berbasis website yang membantu pengguna menemukan sumber berita dari sebuah citra yang mengandung teks berita, misalnya tangkapan layar artikel, potongan berita, atau gambar yang dibagikan melalui media sosial.

Sistem menggunakan RapidOCR untuk mengubah teks pada citra menjadi teks digital. Teks tersebut kemudian diproses untuk memperoleh kata kunci menggunakan TF-IDF. Kata kunci digunakan pada tahap penelusuran sumber berita online. Artikel kandidat yang ditemukan selanjutnya diambil informasinya melalui modul scraping yang disesuaikan dengan struktur halaman sumber. Teks kandidat dibandingkan dengan teks hasil OCR menggunakan Cosine Similarity.

Rujukan utama implementasi web scraping adalah penelitian Hafiz & Sudarmilah (2023), yang menjelaskan proses web scraping portal berita melalui Python dan BeautifulSoup, mulai dari menentukan situs, mengeksplorasi struktur HTML, mengidentifikasi elemen penting seperti judul, URL, isi, tanggal, editor, jurnalis, dan lokasi, sampai menghasilkan data terstruktur/CSV. fileciteturn55file2

### 2. Problem Statement & Bukti

Problem Statement: Pengguna yang hanya memiliki gambar atau tangkapan layar berita dapat kesulitan mengetahui sumber artikel aslinya secara cepat. Pencarian manual berdasarkan potongan teks membutuhkan waktu dan pengguna harus membuka serta membandingkan banyak hasil berita.

Bukti dari jurnal rujukan: artikel menjelaskan bahwa pengumpulan artikel berita secara manual membutuhkan waktu dan upaya, sedangkan web scraping dapat digunakan untuk mengambil data artikel secara otomatis sehingga pengumpulan dan analisis data menjadi lebih cepat dan efisien. fileciteturn55file4

### 3. Target User & Stakeholder

| Aktor/Stakeholder | Peran | Kebutuhan |
| --- | --- | --- |
| Pengguna | Pengguna utama | Mengunggah citra dan memperoleh kandidat sumber berita |
| Pengelola sistem | Pemelihara teknis | Menjaga modul scraping dan konfigurasi sumber |
| Portal berita | Sumber data eksternal | Menyediakan halaman berita yang dapat diakses sesuai ketentuan situs |

### 4. Value Proposition

**Pain:** pencarian sumber dari screenshot dilakukan manual; teks harus diketik ulang; banyak artikel memiliki judul/topik serupa.

**Gain:** teks dapat diekstraksi otomatis, kandidat sumber dapat dikumpulkan, dan artikel dapat diberi nilai kemiripan sehingga pengguna memperoleh daftar sumber yang dapat ditelusuri.

### 5. Tujuan Produk & KPI

| KPI | Target awal |
| --- | --- |
| Ekstraksi teks | Teks hasil OCR dapat digunakan untuk proses pencarian |
| Hasil penelusuran | Sistem menampilkan kandidat artikel yang relevan |
| Similarity | Setiap kandidat memiliki nilai Cosine Similarity |
| Traceability | Setiap hasil memiliki URL sumber |
| Respons sistem | Diukur dari upload sampai hasil ditampilkan |

Target angka performa final harus ditetapkan berdasarkan pengujian dataset penelitian dan tidak diambil sebagai jaminan dari jurnal rujukan.

### 6. Scope Fitur 3 Bulan — MoSCoW

**Must**
- ★ Upload citra
- ★ Ekstraksi teks menggunakan RapidOCR
- ★ Preprocessing teks
- ★ Ekstraksi kata kunci dengan TF-IDF
- ★ Penelusuran sumber berita
- ★ Pengambilan data artikel kandidat
- ★ Perhitungan Cosine Similarity
- ★ Menampilkan ranking sumber

**Should**
- Pratinjau citra
- Menampilkan teks hasil OCR
- Menampilkan cuplikan teks kandidat
- Menampilkan metadata artikel

**Could**
- Filter tanggal
- Filter media/sumber
- Riwayat pencarian

**Won't**
- Menentukan benar/salahnya isi berita secara otomatis
- Menentukan identitas pemilik gambar
- Menyalin penuh isi artikel sebagai database permanen

### 7. Non-Goals

Sistem bukan mesin fact-checking penuh. Nilai similarity menunjukkan kedekatan teks antara input dan kandidat, bukan pembuktian bahwa suatu artikel adalah sumber asli secara mutlak.

### 8. Asumsi & Risiko

- Struktur HTML portal berita dapat berubah.
- Tidak semua halaman berita dapat diakses atau discrape.
- Hasil OCR dipengaruhi kualitas citra.
- Kata kunci yang kurang representatif dapat menghasilkan kandidat yang kurang relevan.
- Nilai similarity bergantung pada preprocessing dan corpus pembanding.
- Pengambilan data harus memperhatikan akses dan kebijakan masing-masing situs.

### 9. Platform & Stack

- Frontend: Next.js / React
- Backend: Python FastAPI
- OCR: RapidOCR
- Text processing: Python, scikit-learn
- Scraping: requests + BeautifulSoup
- Database: SQLite/PostgreSQL untuk metadata/riwayat jika diperlukan

### 10. Acuan Penelitian

Acuan utama proses web scraping adalah Hafiz & Sudarmilah (2023). Penelitian tersebut membagi scraping menjadi pembukaan template, penentuan situs, eksplorasi/navigasi, identifikasi elemen HTML, menjalankan scraping, dan menghasilkan data. fileciteturn55file0
