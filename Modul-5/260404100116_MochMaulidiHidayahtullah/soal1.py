# Fungsi fibonacci menghitung hari
def fibonacci(a):
    if a == 1 or a == 2:
        return 1
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)


# Input hari
n = int(input("Masukkan hari ke: "))

# Menampilkan hasil
if n > 0:
    print("Jumlah pelanggan:", fibonacci(n))
else:
    print("Hari harus lebih dari 0")
