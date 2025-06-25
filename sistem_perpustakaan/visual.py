import matplotlib.pyplot as plt
from collections import Counter
from data_loader import load_data
import os

def tampilkan_grafik():
    buku_list = load_data()

    # Grafik Jumlah Buku per Genre
    genres = [buku['genre'] for buku in buku_list]
    genre_counter = Counter(genres)

    plt.figure(figsize=(8, 5))
    plt.bar(genre_counter.keys(), genre_counter.values(), color='skyblue')
    plt.title("Jumlah Buku per Genre")
    plt.xlabel("Genre")
    plt.ylabel("Jumlah Buku")
    plt.tight_layout()
    plt.savefig("perpustakaan/img/genre_bar.png")
    plt.close()

    # Grafik Status Buku
    status = [buku['status'] for buku in buku_list]
    status_counter = Counter(status)

    plt.figure(figsize=(6, 6))
    plt.pie(status_counter.values(), labels=status_counter.keys(), 
            autopct='%1.1f%%', startangle=90)
    plt.title("Status Buku")
    plt.tight_layout()
    plt.savefig("perpustakaan/img/status_pie.png")
    plt.close()
