import csv
from collections import defaultdict

def load_data():
    buku_list = []
    try:
        with open("perpustakaan/data/daftar_buku.csv", newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                buku_list.append(row)
    except FileNotFoundError:
        print("File data tidak ditemukan.")
    return buku_list

def simpan_data(buku_list):
    with open("perpustakaan/data/daftar_buku.csv", 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['kode', 'judul', 'pengarang', 'tahun', 'genre', 'status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(buku_list)

def hitung_statistik(buku_list):
    result = defaultdict(int)
    for buku in buku_list:
        result[buku['genre']] += 1
        result[buku['status']] += 1
    return result
