def hitung_rata_rata(nilai_list):
    try:
        if not nilai_list: 
            raise ZeroDivisionError("List tidak boleh kosong.")

        for nilai in nilai_list:
            if not isinstance(nilai, (int, float)):
                raise ValueError(f"'{nilai}' bukan angka, silakan masukkan hanya angka.")

        rata_rata = sum(nilai_list) / len(nilai_list)
        return rata_rata

    except ZeroDivisionError as e:
        print(f"Kesalahan: {e}")
    except ValueError as e:
        print(f"Kesalahan: {e}")

def main():
    input_user = input("Masukkan daftar angka (pisahkan dengan koma): ")
    try:
        nilai_list = [float(x.strip()) for x in input_user.split(',')]
        rata_rata = hitung_rata_rata(nilai_list)
        
        if rata_rata is not None:  
            print(f"Rata-rata adalah: {rata_rata}")
            
    except ValueError:
        print("Input tidak valid, silakan masukkan angka dengan benar.")

        
if __name__ == "__main__":
    main()
