kode = int(input("Masukkan kode: "))
digit1 = kode //100
digit2 = (kode //10) % 10
digit3 = kode % 10
print(f"digit pertama: {digit1}, digit kedua: {digit2}, digit ketiga: {digit3}")

nilai_pelacak = digit1 * digit3
print("nilai pelacak =", nilai_pelacak)

if digit2 % 2 != 0:
    nilai_pelacak = nilai_pelacak + 25
else :
    nilai_pelacak = nilai_pelacak - digit2
    print(f"nilai pelacak tahap pertama: {nilai_pelacak}")

if nilai_pelacak % 3 == 0:
    nilai_pelacak = nilai_pelacak // 3
else :
    nilai_pelacak = nilai_pelacak* 2
    print(f"nilai pelacak tahap kedua: {nilai_pelacak}")
if nilai_pelacak > 50:
    print("kategori A")
elif nilai_pelacak > 20:
    print("kategori B")
else:
    print("Ditolak")

if nilai_pelacak % 2 == 0:
    print("siklus pelacak genap")
else:
    print("siklus pelacak ganjil")