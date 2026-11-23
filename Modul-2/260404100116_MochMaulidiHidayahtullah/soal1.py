angka = int(input("Masukkan angka 3 digit: "))

digit1 = angka // 100
digit2 = (angka // 10) % 10
digit3 = angka % 10

nilai_awal = digit1 * digit3

if digit2 % 2 == 1:
    nilai_tahap1 = nilai_awal + 25
else:
    nilai_tahap1 = nilai_awal - digit2

if nilai_tahap1 % 3 == 0:
    nilai_akhir = nilai_tahap1 // 3
else:
    nilai_akhir = nilai_tahap1 * 2

if nilai_akhir > 50:
    status = "Password Kategori A"
elif nilai_akhir > 20:
    status = "Password Kategori B"
else:
    status = "Password Ditolak"

siklus = "Siklus Genap" if nilai_akhir % 2 == 0 else "Siklus Ganjil"

print("Digit pertama:", digit1)
print("Digit kedua:", digit2)
print("Digit ketiga:", digit3)
print("Nilai pelacak awal:", nilai_awal)
print("Nilai pelacak tahap pertama:", nilai_tahap1)
print("Nilai pelacak akhir:", nilai_akhir)
print("Status:", status)
print(siklus)
