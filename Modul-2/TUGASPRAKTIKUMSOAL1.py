kode = int(input("masukkan kode: "))

digit1 = (kode // 100)
print ("digit pertama adalah", digit1)

digit2 = ((kode // 10) % 10)
print ("digit kedua adalah", digit2)

digit3 = (kode % 10)
print ("digit ketiga adalah", digit3)

nilaiPelacak = (digit1 * digit3)
print ("nilai pelacaknya adalah", nilaiPelacak)

#perubahan 1
nilaiAkhir1 = (nilaiPelacak + 25)
nilaiAkhir2 = (nilaiPelacak - digit2)
if digit2 % 2 != 0:
    nilaiPerubahan1 = nilaiAkhir1
    print ("nilai pelacak setelah perubahan pertama adalah", nilaiPerubahan1)
else:
    nilaiPerubahan1 = nilaiAkhir2
    print ("nilai pelacak setelah perubahan pertama adalah", nilaiPerubahan1)

#perubahan 2
nilaiAkhir3 = (nilaiPerubahan1 // 3)
nilaiAkhir4 = (nilaiPerubahan1 * 2)
if nilaiPerubahan1 % 3 == 0:
    nilaiPerubahan2 = nilaiAkhir3
    print ("nilai akhirnya adalah", nilaiAkhir3)
else:
    nilaiPerubahan2 = nilaiAkhir4
    print ("nilai akhirnya adalah", nilaiAkhir4)

#3
if nilaiPerubahan2 >50:
    print ("Kategori A")
elif nilaiPerubahan2 >20 and nilaiPerubahan2 <50:
    print ("Kategori B")
else:
    print ("Password Ditolak")