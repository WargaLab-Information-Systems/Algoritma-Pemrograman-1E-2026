while True:
    n = int(input("Masukkan angka bilangan bulat positif: "))
    if n > 0:
        break
    print("Masukkan nilai valid!")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')

    for j in range(1, 4 * (n - i) + n):
        print(' ', end='')

    for j in range(i, 0, -1):
        print(j, end=' ')

    print()
