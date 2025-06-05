class JumlahOrangException(Exception):
    pass

def input_jumlah_orang():
    while True:
        try:
            jumlah = int(input("Masukkan jumlah orang: "))
            if jumlah <= 0:
                raise JumlahOrangException("Jumlah orang tidak valid (harus > 0)")
            for i in range(1, jumlah + 1):
                print(f"Orang ke-{i}")
            break
        except JumlahOrangException as e:
            print(e)
        except ValueError:
            print("Input harus berupa angka.")

input_jumlah_orang()
