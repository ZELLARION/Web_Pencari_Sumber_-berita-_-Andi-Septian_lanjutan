# ACCEPTANCE CRITERIA

## US-01 — Upload Citra

- [ ] Pengguna dapat memilih file citra.
- [ ] Sistem menolak file yang tidak didukung.
- [ ] Sistem memulai proses setelah file valid.

## US-02 — Ekstraksi Teks

- [ ] RapidOCR dipanggil setelah citra valid.
- [ ] Teks OCR tersedia sebagai output.
- [ ] Jika tidak ada teks, sistem menampilkan pesan.

## US-03 — Penelusuran Sumber

- [ ] Sistem menghasilkan kata kunci.
- [ ] Kata kunci digunakan untuk penelusuran.
- [ ] Kandidat URL dapat dikumpulkan.

## US-04 — Perbandingan Kandidat

- [ ] Artikel kandidat diproses.
- [ ] Similarity score dihitung.
- [ ] Kandidat diurutkan berdasarkan score.

## US-05 — Membuka Sumber

- [ ] Setiap hasil memiliki URL jika tersedia.
- [ ] URL dapat dibuka pengguna.
- [ ] Sistem tidak menyatakan similarity sebagai bukti final kebenaran berita.
