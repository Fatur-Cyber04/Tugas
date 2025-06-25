from katalog import tampilkan_buku, cari_buku
from pinjam import pinjam_buku, kembalikan_buku
from visual import tampilkan_grafik
import os

def buat_folder_dan_file_jika_tidak_ada():
    # Create folders if not exist
    if not os.path.exists('perpustakaan/data'):
        os.makedirs('perpustakaan/data')
    if not os.path.exists('perpustakaan/img'):
        os.makedirs('perpustakaan/img')
        
    if not os.path.exists('perpustakaan/data/daftar_buku.csv'):
        with open('perpustakaan/data/daftar_buku.csv', 'w', encoding='utf-8') as f:
            f.write('kode,judul,pengarang,tahun,genre,status\n')
            f.write('B001,Laskar Pelangi,Andrea Hirata,2005,Fiksi,Tersedia\n')
            f.write('B002,Python untuk Pemula,Andi Setiawan,2022,Komputer,Tersedia\n')
            f.write('B003,Sang Pemimpi,Andrea Hirata,2006,Fiksi,Dipinjam\n')
            f.write('B004,Matematika Dasar,Budi Santoso,2019,Edukasi,Tersedia\n')
            f.write('B005,1984,George Orwell,1949,Fiksi,Tersedia\n')
            f.write('B006,Belajar Machine Learning,Joko Susilo,2021,Komputer,Tersedia\n')
            f.write('B007,The Great Gatsby,F. Scott Fitzgerald,1925,Fiksi,Dipinjam\n')
            f.write('B008,Dasar-Dasar Statistik,Rina Sari,2020,Edukasi,Tersedia\n')
            f.write('B009,Clean Code,Robert C. Martin,2008,Komputer,Tersedia\n')
            f.write('B010,Sapiens: A Brief History of Humankind,Yuval Noah Harari,2011,Non-Fiksi,Tersedia\n')

def main():
    buat_folder_dan_file_jika_tidak_ada()
    
    while True:
        print("\n===== SISTEM PERPUSTAKAAN MINI =====")
        print("1. Tampilkan semua buku")
        print("2. Cari buku")
        print("3. Pinjam buku")
        print("4. Kembalikan buku")
        print("5. Tampilkan grafik")
        print("0. Keluar")
        
        try:
            pilihan = input("Pilih menu: ")
            
            if pilihan == "1":
                print("\n=== DAFTAR BUKU ===")
                tampilkan_buku()
                
            elif pilihan == "2":
                print("\n=== PENCARIAN BUKU ===")
                cari_buku()
                
            elif pilihan == "3":
                print("\n=== PEMINJAMAN BUKU ===")
                pinjam_buku()
                
            elif pilihan == "4":
                print("\n=== PENGEMBALIAN BUKU ===")
                kembalikan_buku()
                
            elif pilihan == "5":
                print("\n=== STATISTIK BUKU ===")
                tampilkan_grafik()
                print("Grafik berhasil dibuat di folder perpustakaan/img")
                
            elif pilihan == "0":
                print("\nTerima kasih telah menggunakan sistem perpustakaan mini!")
                break
                
            else:
                print("\nPilihan tidak valid! Silakan pilih 0-5")
                
        except Exception as e:
            print(f"\nTerjadi kesalahan: {str(e)}")
            print("Silakan coba lagi")

if __name__ == "__main__":
    main()
