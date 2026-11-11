def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) +  fibonacci (n-2)
n = int(input("Masukkan hari ke - N: "))

if n > 0 :
    hasil = fibonacci(n)
    print("Jumlah pelanggan hari ke-", n, ":", hasil)
else:
    print("Input harus bilangan bulat positif!")