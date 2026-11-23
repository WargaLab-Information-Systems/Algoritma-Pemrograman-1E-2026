n = int(input("masukkan nilai n (bilangan bulat positif): "))
for i in range(1, n + 1):
    j = n - i + 1

    for spasi in range(n - i):
        print("  ", end="")
    for naik in range(1, i + 1):
        print(naik, end=" ")
    for turun in range(i - 1, 0, -1):
        print(turun, end=" ")
    for spasi in range(n - i):   
        print("  ", end="")

    print("   ", end="")  

    for spasi in range(n - j):
        print("  ", end="")
    for naik in range(1, j + 1):
        print(naik, end=" ")
    for turun in range(j - 1, 0, -1):
        print(turun, end=" ")

    print()