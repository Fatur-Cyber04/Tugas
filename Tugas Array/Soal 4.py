rak_tahu = [10, 10, 10, 10, 10, 10, 10, 10]

harga_per_tahu = 1000

uang_input = 100000
jumlah_tahu_dibeli = 20

total_harga = jumlah_tahu_dibeli * harga_per_tahu

if uang_input >= total_harga:
    uang_kembali = uang_input - total_harga

    for i in range(len(rak_tahu)):
        if rak_tahu[i] > 0 and jumlah_tahu_dibeli > 0:
            if rak_tahu[i] >= jumlah_tahu_dibeli:
                rak_tahu[i] -= jumlah_tahu_dibeli
                jumlah_tahu_dibeli = 0
            else:
                jumlah_tahu_dibeli -= rak_tahu[i]
                rak_tahu[i] = 0

    print(f"Total harga yang dibeli: {total_harga}")
    print(f"Uang Kembali: {uang_kembali}")
    print(f"Sisa Tahu: {sum(rak_tahu)}")
    print(f"Posisi Akhir Rak: {rak_tahu}")

else:
    print("Uang tidak cukup untuk membeli tahu.")
