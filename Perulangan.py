menu = [
    "Hitung luas segitiga",
    "Hitung luas persegi panjang",
    "Menentukan angka ganjil dan genap",
    "Quit"
]

pilihan = "0"

while pilihan != "4":
    print("\nMenu:")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

    pilihan = input("Pilih menu (1/2/3/4): ")

    match pilihan:
        case "1":
            alas = float(input("Masukkan alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas = 0.5 * alas * tinggi
            print(f"Luas segitiga adalah: {luas:.2f}")

        case "2":
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            luas = panjang * lebar
            print(f"Luas persegi panjang adalah: {luas:.2f}")

        case "3":
            angka = int(input("Masukkan angka: "))
            if angka % 2 == 0:
                print(f"{angka} adalah bilangan genap.")
            else:
                print(f"{angka} adalah bilangan ganjil.")

        case "4":
            print("Terima kasih, program selesai.")

        case _:
            print("Pilihan tidak valid.")