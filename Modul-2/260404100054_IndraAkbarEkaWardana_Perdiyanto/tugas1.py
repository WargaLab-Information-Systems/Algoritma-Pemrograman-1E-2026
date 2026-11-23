kode = int(input("Masukkan kode 3 digit: "))

digit1 = kode // 100
digit2 = (kode // 10) % 10
digit3 = kode % 10

print("Digit pertama :", digit1)
print("Digit kedua   :", digit2)
print("Digit ketiga  :", digit3)

pelacak = digit1 * digit3
print("Nilai pelacak awal :", pelacak)

if digit2 % 2 == 1:
    pelacak = pelacak + 25
else:
    pelacak = pelacak - digit2

print("Pelacak setelah tahap pertama :", pelacak)

if pelacak % 3 == 0:
    pelacak = pelacak // 3
else:
    pelacak = pelacak * 2

print("Nilai akhir :", pelacak)

if pelacak > 50:
    print("Status Password : Kategori A")
elif pelacak > 20:
    print("Status Password : Kategori B")
else:
    print("Status Password : Password Ditolak")

if pelacak % 2 == 0:
    print("Siklus Genap")
else:
    print("Siklus Ganjil")
