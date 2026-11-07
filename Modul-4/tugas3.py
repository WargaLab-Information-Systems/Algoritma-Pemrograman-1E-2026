n = int(input("Masukkan Bilangan Bulat Positif :"))

for i in range (1, n+1):
    for a in range (1, i+1):
        print(a, end=" ")
    for b in range (2 * (n-i) + 1):
        print(" ", end=" ")
    for a in range (i, 0, -1):
        print(a, end=" ")
    print()