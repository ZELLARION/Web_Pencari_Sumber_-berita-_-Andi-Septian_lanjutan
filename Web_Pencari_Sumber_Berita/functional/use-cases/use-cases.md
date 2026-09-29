# USE CASES

## UC-01 — Mencari Sumber Berita dari Citra

**Aktor:** Pengguna

**Tujuan:** memperoleh kandidat sumber berita dari citra yang mengandung teks.

### Precondition

* Website dapat diakses.
* Pengguna memiliki citra input.
* Koneksi internet tersedia untuk penelusuran.

### Main Flow

1. Pengguna memilih citra.
2. Sistem memvalidasi file.
3. Sistem mengirim citra ke backend.
4. RapidOCR mengekstraksi teks.
5. Sistem melakukan preprocessing.
6. TF-IDF menghasilkan kata berbobot.
7. Sistem membentuk query/kata kunci.
8. Sistem melakukan penelusuran.
9. Sistem mengambil URL kandidat.
10. Scraper mengambil data artikel.
11. Sistem menghitung Cosine Similarity.
12. Sistem mengurutkan kandidat.
13. Sistem menampilkan hasil kepada pengguna.

### Alternative Flow

**A1 — File tidak valid**
1. Sistem menolak file.
2. Sistem menampilkan pesan kesalahan.

**A2 — OCR gagal**
1. Sistem tidak menemukan teks.
2. Sistem meminta citra yang lebih jelas.

**A3 — Artikel gagal diambil**
1. Kandidat ditandai gagal.
2. Sistem melanjutkan kandidat berikutnya.

### Postcondition

Pengguna memperoleh daftar kandidat sumber dengan URL dan similarity score.

---

## UC-02 — Melihat Detail Kandidat

**Aktor:** Pengguna

1. Pengguna memilih kandidat.
2. Sistem menampilkan metadata yang tersedia.
3. Pengguna dapat membuka URL sumber.

---

## UC-03 — Melihat Teks OCR

**Aktor:** Pengguna

1. Pengguna menyelesaikan proses pencarian.
2. Sistem menampilkan teks hasil OCR.
3. Pengguna dapat membandingkan teks OCR dengan kandidat.
