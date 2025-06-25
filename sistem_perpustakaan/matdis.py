def hitung_nilai_y():
    print(f"Algoritma ini menghitung nilai y dari persamaan y = 3x + 8 pengguna diminta untuk memasukkan nilai x.")

    while True:
        try:
            nilai_x_str = input("Masukkan nilai x: ")
            nilai_x = float(nilai_x_str) 
            break 
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    nilai_y = (3 * nilai_x) + 8
    print(f"Nilai y dari persamaan 3x + 8 adalah: {nilai_y}")

hitung_nilai_y()