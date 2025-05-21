def jumlah_dua_list(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print("Hasil penjumlahan dua list:", jumlah_dua_list(list_a, list_b))#Soal 3