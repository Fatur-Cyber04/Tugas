from data_loader import load_data

def tampilkan_buku():
    buku_list = load_data()
    print("\nDaftar Buku:")
    for buku in buku_list:
        print(f"{buku['kode']} | {buku['judul']} - {buku['pengarang']} ({buku['tahun']}) | {buku['genre']} | Status: {buku['status']}")

def cari_buku():
    keyword = input("Masukkan judul/genre/tahun: ").lower()
    buku_list = load_data()
    hasil = [b for b in buku_list if keyword in b['judul'].lower() or keyword in b['genre'].lower() or keyword in b['tahun']]
    
    if hasil:
        print("\nHasil Pencarian:")
        for buku in hasil:
            print(f"{buku['kode']} | {buku['judul']} - {buku['pengarang']} ({buku['tahun']}) | {buku['genre']} | Status: {buku['status']}")
    else:
        print("Buku tidak ditemukan.")
