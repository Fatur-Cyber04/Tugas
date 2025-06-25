from data_loader import load_data, simpan_data

def pinjam_buku():
    kode = input("Masukkan kode buku: ").upper()
    buku_list = load_data()
    for buku in buku_list:
        if buku['kode'] == kode:
            if buku['status'] == "Tersedia":
                buku['status'] = "Dipinjam"
                simpan_data(buku_list)
                print(f"Buku '{buku['judul']}' berhasil dipinjam.")
                return
            else:
                print("Buku sedang dipinjam.")
                return
    print("Kode buku tidak ditemukan.")

def kembalikan_buku():
    kode = input("Masukkan kode buku: ").upper()
    buku_list = load_data()
    for buku in buku_list:
        if buku['kode'] == kode:
            if buku['status'] == "Dipinjam":
                buku['status'] = "Tersedia"
                simpan_data(buku_list)
                print(f"Buku '{buku['judul']}' berhasil dikembalikan.")
                return
            else:
                print("Buku belum dipinjam.")
                return
    print("Kode buku tidak ditemukan.")
