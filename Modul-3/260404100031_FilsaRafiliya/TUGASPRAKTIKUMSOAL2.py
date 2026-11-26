while True:
    baris = int(input("masukkan tinggi menara: "))
    if baris >=2 and baris <=15:
        break
    print ("nilai tidak valid")

for o in range (1, baris + 1):
    for b in range (baris - o):
        print(" ", end="")

    for c in range(1, o + 1):
        print(c % 10, end="")

    for c in range(o - 1, 0, -1):
        print(c % 10, end="")
    print ()

for o in range(baris -1, 0, -1):
    for b in range(baris -o):
        print(" ", end="")

    for c in range(1, o + 1):
        print(c % 10, end="")

    for c in range(o - 1, 0, -1):
        print(c % 10, end="")
    print()