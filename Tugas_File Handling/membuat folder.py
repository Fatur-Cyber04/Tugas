import os

# Membuat folder
folder_name = "fatur"
os.makedirs(folder_name, exist_ok=True)

# Membuat dan menulis file
file_path = os.path.join(folder_name, "fatur.txt")
with open(file_path, 'w') as file:
    file.write("Nama: Faturahman\n")
    file.write("Usia: 22\n")
    file.write("Alamat: Jakarta\n")

# Membaca dan menampilkan isi file
with open(file_path, 'r') as file:
    data = file.read()
    print(data)
