while True:
    baris = int(input("masukkan angka:"))
    if baris > 2 and baris < 15:
        break
    print("Masukan nilai valid")

for i in range(1, baris + 1):
    for j in range (baris - i):
        print(" ", end="")

    for k in range(1, i + 1):
        print(k % 10,  end="")

    for k in range(i -1, 0, -1):
        print(k % 10,  end="")

    print()
for i in range(baris -1, 0, -1):
    for j in range(baris -i):
        print(" ", end="")

    for k in range(1, i + 1):
        print(k % 10, end="")

    for k in range(i -1, 0, - 1):
        print(k % 10, end="")
    print()