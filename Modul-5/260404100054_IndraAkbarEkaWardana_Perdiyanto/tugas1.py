def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

hari = int(input("Masuk kan hari ke: "))

if hari >= 1:
    hasil = fibonacci(hari)
    print("Jumlah pelanggan:", hasil)
else:
    print("Hari harus lebih dari 0")
