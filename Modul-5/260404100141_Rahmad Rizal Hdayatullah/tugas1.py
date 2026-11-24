def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("PROGRAM JUMLAH PELANGGAN TOKO KUE")



hari = int(input("Masukkan hari ke-N: "))

if hari <= 0:
    print("\nPeringatan! Hari harus berupa bilangan bulat positif.")

else:

    jumlah = fibonacci(hari)


    print("\n HASIL PERHITUNGAN")
    print("Hari ke-", hari)
    print("Jumlah pelanggan:", jumlah, "orang")
    print("=======================================")

