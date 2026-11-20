# Pendeteksi TODO, Fungsi Panjang, dan Error Sintaks (`cek.py`)

Tool CLI analisis kode statis sederhana berbasis **Tree-sitter** untuk memindai seluruh file Python (`.py`) di dalam sebuah direktori secara rekursif. Proyek ini dibuat sebagai bagian dari **Tugas 6 — Materi & Tugas Awal: Memahami Tree-sitter**.

## Fitur Utama

1. **Deteksi Komentar `TODO` dan `FIXME`**
   Mencari seluruh node komentar (`comment`) yang mengandung kata kunci `TODO` atau `FIXME` menggunakan query S-expression dengan predikat `#match?`, lalu melaporkan lokasi file dan nomor barisnya.
2. **Deteksi Fungsi Panjang (> 30 Baris)**
   Mencari definisi fungsi (`function_definition`) dan menghitung panjang barisnya menggunakan selisih posisi `end_point` dan `start_point`. Fungsi yang memiliki lebih dari 30 baris akan dilaporkan beserta nama dan total barisnya.
3. **Deteksi Error Sintaks**
   Memeriksa atribut `tree.root_node.has_error` pada setiap file yang di-parse. Jika ditemukan kesalahan sintaks, program akan menelusuri pohon untuk melaporkan posisi baris pertama yang bermasalah (`ERROR` atau `MISSING`).

## Prasyarat & Instalasi Dependensi

Pastikan **Python 3.10+** sudah terpasang di sistem Anda, kemudian pasang library binding Python Tree-sitter beserta grammar Python:

```bash
pip install tree-sitter tree-sitter-python
```

*(Opsional)* Jika Anda mengaktifkan dukungan pengayaan untuk memindai file JavaScript (`.js`), pasang juga grammar JavaScript:

```bash
pip install tree-sitter-javascript
```

## Struktur Direktori

```text
.
├── cek.py                  # Skrip utama CLI analisis kode
├── README.md               # Dokumentasi proyek
└── uji/                    # Folder berisi sampel uji lokal
    ├── ada_todo.py         # Sampel komentar TODO dan FIXME
    ├── fungsi_panjang.py   # Sampel fungsi dengan panjang > 30 baris
    └── sintaks_rusak.py    # Sampel kode dengan sintaks tidak valid
```

## Cara Menjalankan

Jalankan `cek.py` melalui terminal dengan menyertakan path folder target sebagai argumen:

```bash
python cek.py <folder_target>
```

### 1. Menjalankan pada Folder Uji Lokal

```bash
python cek.py uji/
```

### 2. Menjalankan pada Repositori Proyek Nyata

```bash
git clone <url-repositori-python> contoh-repo
python cek.py contoh-repo/
```

> **Catatan Performa:** Pemindaian otomatis melewati direktori lingkungan dan metadata seperti `venv/`, `.venv/`, `.git/`, `node_modules/`, dan `__pycache__/` agar proses analisis berjalan cepat.

## Contoh Output

Hasil eksekusi perintah `python cek.py uji/` pada ketiga file sampel lokal:

```text
[TODO]    uji/ada_todo.py:4: # TODO: tambahkan validasi jika persen negatif atau > 100
[TODO]    uji/ada_todo.py:12: # FIXME: tangani kasus jika kunci 'harga' tidak ada di dictionary
[PANJANG] uji/fungsi_panjang.py:7: fungsi 'validasi_dan_ringkas_transaksi' (38 baris)
[ERROR]   uji/sintaks_rusak.py:3: sintaks tidak valid (MISSING)
```

## Catatan Teknis & Batasan

- **Perhitungan Semua Jenis Fungsi:** Pemeriksaan fungsi panjang menghitung seluruh kemunculan node `function_definition`, termasuk method di dalam kelas (*class method*) maupun fungsi bersarang (*nested function*).
- **Penanganan Encoding File:** Dekode teks sumber menggunakan `decode(errors="replace")` untuk mencegah `UnicodeDecodeError` saat memindai repositori yang memiliki karakter non-UTF-8.
- **Verifikasi Manual pada Repositori Nyata:** Sebelum mengumpulkan tugas, pastikan Anda telah menguji `cek.py` pada satu repositori Python open-source dan mencocokkan output-nya secara manual pada minimal 2 file acak.