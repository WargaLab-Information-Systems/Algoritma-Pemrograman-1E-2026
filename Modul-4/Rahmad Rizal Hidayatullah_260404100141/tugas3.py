while True:
    n = input("Masukkan bilangan bulat positif: ")

    valid = True

    for angka in n:
        if angka < "0" or angka > "9":
            valid = False

    if valid and n != "":
        n = int(n)

        if n > 0:
            break
        else:
            print("Peringatan! Angka harus lebih dari 0!")
    else:
        print("Peringatan! Masukkan bilangan bulat positif!")


for i in range(1, n + 1):


    for j in range(1, i + 1):
        print(j, end="")


    if i < n:
        for spasi in range(2 * (n - i)):
            print(" ", end="")
    elif i == n:
        print("", end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()
