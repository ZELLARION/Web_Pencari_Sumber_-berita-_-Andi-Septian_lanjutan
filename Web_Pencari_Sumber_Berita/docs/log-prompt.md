# LOG PROMPT

## Tujuan

Mencatat keputusan perancangan utama project.

### Keputusan 01 — OCR

RapidOCR dipilih sebagai komponen ekstraksi teks karena project membutuhkan pengubahan teks pada citra menjadi teks yang dapat diproses.

### Keputusan 02 — Penelusuran

Teks OCR tidak langsung dianggap sebagai sumber. Sistem membentuk kata kunci lalu menelusuri sumber berita untuk memperoleh kandidat.

### Keputusan 03 — Scraping

Jurnal Hafiz & Sudarmilah digunakan sebagai acuan alur scraping: menentukan situs, mengeksplorasi struktur HTML, mengidentifikasi elemen, menjalankan scraping, dan menghasilkan data. fileciteturn55file1

### Keputusan 04 — Similarity

Cosine Similarity digunakan untuk membandingkan representasi teks input dengan artikel kandidat.

### Keputusan 05 — Output

Hasil menampilkan URL sehingga pengguna dapat melakukan pemeriksaan langsung terhadap sumber.
