# Sistem Katalog & Peminjaman Buku

## Deskripsi
Aplikasi katalog buku mini berbasis CLI untuk mencari dan mencatat peminjaman/pengembalian buku, serta menampilkan statistik visual.

## Struktur Proyek
- `main.py`: Menu utama dan navigasi
- `katalog.py`: Fungsi tampilan dan pencarian buku
- `pinjam.py`: Fungsi peminjaman dan pengembalian
- `data_loader.py`: Fungsi load/simpan file CSV
- `visual.py`: Visualisasi data menggunakan matplotlib/seaborn
- `data/daftar_buku.csv`: Database buku
- `img/`: Folder penyimpanan grafik

## Cara Menjalankan
```bash
python main.py
