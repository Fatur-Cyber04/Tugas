import array as arr

kamar = arr.array('u', [])


for i in range(10):
    if i+1 == 2 or i+1 == 4 or i+1 == 7 or i+1 == 9:
        kamar.insert(i, 'O')
    else:
        kamar.insert(i, 'X')

print("Sebelum dihapus:", kamar)

while len(kamar) > 0:
    kamar.remove(kamar[0])  

print("Setelah kamar kost dirobohkan:", kamar)
