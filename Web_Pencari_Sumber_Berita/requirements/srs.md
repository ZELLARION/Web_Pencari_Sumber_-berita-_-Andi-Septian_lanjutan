# DRAF SRS (SOFTWARE REQUIREMENTS SPECIFICATION)

## Web Pencari Sumber Berita Berbasis Ekstraksi Teks Citra

---

## 1. Tujuan, Scope, dan Definisi Istilah

### 1.1 Tujuan

Sistem bertujuan membantu pengguna menelusuri sumber berita berdasarkan teks yang diperoleh dari citra. Sistem mengubah citra menjadi teks, memproses teks untuk memperoleh kata kunci, mencari artikel kandidat, kemudian membandingkan teks input dengan teks artikel menggunakan Cosine Similarity.

### 1.2 Scope Sistem

**Dalam scope:**
* Upload citra.
* Ekstraksi teks menggunakan RapidOCR.
* Preprocessing teks.
* Ekstraksi kata kunci menggunakan TF-IDF.
* Penelusuran sumber berita online.
* Pengambilan data artikel kandidat.
* Perhitungan Cosine Similarity.
* Ranking kandidat berdasarkan similarity.
* Menampilkan URL dan metadata sumber.

**Di luar scope:**
* Identifikasi pemilik gambar.
* Pemberian keputusan final bahwa artikel tertentu adalah sumber asli.
* Fact-checking isi berita secara penuh.
* Penyimpanan permanen seluruh isi artikel pihak ketiga.

### 1.3 Definisi Istilah

| Istilah | Definisi |
| --- | --- |
| **OCR** | Teknologi untuk mengubah teks pada citra menjadi teks digital. |
| **RapidOCR** | Engine OCR yang digunakan sistem untuk ekstraksi teks dari citra. |
| **Preprocessing** | Tahap membersihkan dan menormalisasi teks sebelum analisis. |
| **TF-IDF** | Pembobotan kata berdasarkan frekuensi pada dokumen dan kekhususannya terhadap kumpulan dokumen. |
| **Cosine Similarity** | Ukuran kemiripan antara dua vektor teks berdasarkan sudut antar-vektor. |
| **Web Scraping** | Pengambilan data dari halaman web untuk diproses lebih lanjut. |
| **Artikel Kandidat** | Artikel berita yang diperoleh pada tahap penelusuran dan dibandingkan dengan teks OCR. |
| **Similarity Score** | Nilai kemiripan antara teks input dan teks artikel kandidat. |

---

# 2. User, Stakeholder, Lingkungan Operasi, Asumsi & Dependensi

### 2.1 User dan Stakeholder

| Aktor | Peran | Kebutuhan |
| --- | --- | --- |
| Pengguna | Pengguna utama | Mengunggah citra dan memperoleh sumber kandidat |
| Pengelola sistem | Pemelihara | Memperbarui konfigurasi scraper bila struktur situs berubah |
| Portal berita | Sistem eksternal | Menjadi sumber halaman artikel |

### 2.2 Lingkungan Operasi

Sistem digunakan pada:
* Platform website.
* Browser modern.
* Perangkat yang dapat mengunggah citra.
* Koneksi internet pada saat penelusuran dan pengambilan artikel.

### 2.3 Asumsi

| ID | Asumsi |
| --- | --- |
| AS-01 | Citra yang diunggah mengandung teks yang dapat dikenali OCR. |
| AS-02 | Portal berita kandidat dapat diakses saat proses berlangsung. |
| AS-03 | Struktur halaman sumber dapat dipetakan oleh scraper. |
| AS-04 | Teks OCR cukup informatif untuk membentuk query/kata kunci. |
| AS-05 | Nilai similarity digunakan sebagai indikator relevansi, bukan keputusan kebenaran berita. |

### 2.4 Dependensi

| ID | Dependensi |
| --- | --- |
| DEP-01 | RapidOCR untuk ekstraksi teks citra. |
| DEP-02 | Library Python untuk preprocessing dan TF-IDF. |
| DEP-03 | Modul HTTP dan HTML parser untuk mengambil artikel kandidat. |
| DEP-04 | Ketersediaan koneksi internet. |
| DEP-05 | Struktur HTML situs sumber yang dapat diidentifikasi. |

---

# 3. Functional Requirements

| ID | Requirement | Prioritas | Metode Verifikasi |
| --- | --- | --- | --- |
| **FR-01** | Sistem harus dapat **menerima citra saat pengguna melakukan upload** → sistem memperoleh file citra untuk diproses. | **Must** | Pengujian |
| **FR-02** | Sistem harus dapat **mengekstraksi teks dari citra menggunakan RapidOCR saat citra valid** → menghasilkan teks OCR. | **Must** | Pengujian OCR |
| **FR-03** | Sistem harus dapat **melakukan preprocessing terhadap teks OCR** → menghasilkan teks yang lebih siap untuk analisis. | **Must** | Pengujian fungsional |
| **FR-04** | Sistem harus dapat **menghasilkan bobot TF-IDF dari teks input** → menghasilkan representasi/bobot kata. | **Must** | Pengujian unit |
| **FR-05** | Sistem harus dapat **menghasilkan kata kunci untuk penelusuran** → menghasilkan query/kumpulan kata kunci. | **Must** | Pengujian fungsional |
| **FR-06** | Sistem harus dapat **menelusuri sumber berita berdasarkan kata kunci** → menghasilkan daftar kandidat artikel. | **Must** | Pengujian integrasi |
| **FR-07** | Sistem harus dapat **mengambil metadata dan teks artikel kandidat** → menghasilkan data artikel yang dapat dibandingkan. | **Must** | Pengujian scraping |
| **FR-08** | Sistem harus dapat **menghitung Cosine Similarity antara teks OCR dan artikel kandidat** → menghasilkan similarity score. | **Must** | Pengujian algoritmik |
| **FR-09** | Sistem harus dapat **mengurutkan kandidat berdasarkan similarity score** → menghasilkan ranking sumber. | **Must** | Pengujian algoritmik |
| **FR-10** | Sistem harus dapat **menampilkan hasil penelusuran** → menampilkan URL, judul, metadata, dan nilai similarity kandidat. | **Must** | Pengujian UI |
| **FR-11** | Sistem dapat **menampilkan teks hasil OCR** → pengguna dapat memeriksa hasil ekstraksi. | **Should** | Pengujian UI |
| **FR-12** | Sistem dapat **menyimpan riwayat pencarian jika fitur diaktifkan** → menghasilkan daftar pencarian sebelumnya. | **Could** | Pengujian database |

---

# 4. Non-Functional Requirements

| ID | Kategori | Requirement | Metrik | Target | Kondisi Ukur |
| --- | --- | --- | --- | --- | --- |
| **NFR-01** | Performance | Sistem harus menyelesaikan pipeline dalam waktu yang dapat diterima. | Waktu proses | Diukur dan dilaporkan | Dataset uji |
| **NFR-02** | Accuracy | Hasil OCR dan similarity harus dapat dievaluasi menggunakan dataset berlabel. | OCR / retrieval metric | Ditetapkan setelah dataset final | Dataset uji |
| **NFR-03** | Usability | Pengguna dapat mengunggah citra dan memahami hasil tanpa konfigurasi teknis. | Keberhasilan task | ≥95% task uji | Uji pengguna |
| **NFR-04** | Reliability | Kegagalan OCR, pencarian, atau scraping tidak menyebabkan aplikasi crash. | Error handling | 100% skenario uji | Uji skenario |
| **NFR-05** | Security | File input dan data hasil proses diproses hanya sesuai kebutuhan aplikasi. | Audit penyimpanan | Sesuai kebijakan sistem | Pemeriksaan storage |
| **NFR-06** | Maintainability | Selector/konfigurasi scraper dapat diperbarui tanpa mengubah seluruh pipeline. | Modifikasi komponen | Terisolasi pada adapter sumber | Review kode |

### Catatan

Jurnal rujukan membuktikan pola scraping portal berita dan menghasilkan data seperti media, judul, URL, isi, tanggal, editor, jurnalis, dan lokasi. Jurnal tersebut tidak menetapkan target performa untuk sistem pencari sumber ini, sehingga target kuantitatif prototype harus diperoleh melalui pengujian sendiri. fileciteturn55file6

---

# 5. Kebutuhan Data Minimum Fitur

| Fitur | Input | Output |
| --- | --- | --- |
| ★ OCR | Citra | Teks OCR |
| ★ Preprocessing | Teks OCR | Teks bersih |
| ★ TF-IDF | Teks bersih | Bobot kata |
| ★ Keyword extraction | Bobot TF-IDF | Kata kunci/query |
| ★ Search | Kata kunci | Kandidat artikel |
| ★ Scraping | URL kandidat | Metadata + teks artikel |
| ★ Similarity | Teks OCR + teks artikel | Similarity score |
| ★ Ranking | Kandidat + score | Urutan sumber |

### Data Artikel Kandidat

Minimum:
* Media/sumber
* Judul
* URL
* Isi artikel yang diperlukan untuk perbandingan
* Tanggal bila tersedia

Field tersebut mengikuti elemen data yang dibahas pada jurnal rujukan. fileciteturn55file6

---

# 6. Aturan Bisnis

### BR-01 — Sumber Kandidat

Hasil penelusuran merupakan kandidat sumber yang diperoleh berdasarkan kata kunci dari teks citra.

### BR-02 — Similarity

Semakin tinggi nilai Cosine Similarity, semakin dekat representasi teks kandidat terhadap teks input berdasarkan corpus dan preprocessing yang digunakan.

### BR-03 — Ranking

Kandidat diurutkan berdasarkan similarity score dari nilai yang lebih tinggi ke lebih rendah.

### BR-04 — Transparansi

Setiap kandidat harus menampilkan URL sumber agar pengguna dapat membuka dan memeriksa artikel asli secara langsung.

### BR-05 — Scraping

Scraper mengikuti tahapan penentuan situs, eksplorasi struktur HTML, identifikasi elemen penting, menjalankan scraping, dan menghasilkan data terstruktur sebagaimana pola pada jurnal rujukan. fileciteturn55file0

### BR-06 — Batas Interpretasi

Similarity score tidak boleh diperlakukan sebagai bukti tunggal bahwa sebuah artikel merupakan sumber asli atau bahwa isi berita benar.

---

# 7. Matriks Traceability

| Requirement SRS | Fitur/Elemen PRD Terkait | Sumber |
| --- | --- | --- |
| **FR-01** | Upload citra | PRD Scope |
| **FR-02** | RapidOCR | PRD Scope |
| **FR-03** | Preprocessing | PRD Scope |
| **FR-04** | TF-IDF | PRD Scope |
| **FR-05** | Ekstraksi kata kunci | PRD Scope |
| **FR-06** | Penelusuran sumber | PRD Scope |
| **FR-07** | Scraping artikel | Jurnal rujukan |
| **FR-08** | Cosine Similarity | PRD Scope |
| **FR-09** | Ranking sumber | PRD Scope |
| **FR-10** | Hasil pencarian | PRD Scope |
| **FR-11** | Teks OCR | PRD Should Have |
| **FR-12** | Riwayat | PRD Could Have |
| **NFR-01** | Waktu proses | PRD KPI |
| **NFR-02** | Evaluasi OCR/retrieval | PRD KPI |
| **NFR-03** | Kemudahan penggunaan | PRD KPI |
| **NFR-04** | Error handling | PRD KPI |
| **NFR-05** | Keamanan data | PRD NFR |
| **NFR-06** | Modularitas scraper | PRD NFR |

### Kesimpulan SRS

SRS mendefinisikan perilaku yang harus disediakan sistem. Detail arsitektur, struktur class, endpoint, database schema, dan implementasi library ditempatkan pada HLD/LLD.
