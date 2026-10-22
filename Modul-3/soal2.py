tinggi = int(input("Masukkan tinggi setengah menara (2-15): "))
while tinggi < 2 or tinggi > 15:
    tinggi = int(input("Input salah, masukkan angka 2-15: "))
for baris in range(1, tinggi + 1):
    print("  " * (tinggi - baris), end="")
    for angka in range(1, baris + 1):
        print(angka % 10, end=" ")
    for angka in range(baris - 1, 0, -1):
        print(angka % 10, end=" ")
    print()
for baris in range(tinggi - 1, 0, -1):
    print("  " * (tinggi - baris), end="")
    for angka in range(1, baris + 1):
        print(angka % 10, end=" ")
    for angka in range(baris - 1, 0, -1):
        print(angka % 10, end=" ")
    print()