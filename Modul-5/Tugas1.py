def hitung_pelanggan(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return hitung_pelanggan(n-1) + hitung_pelanggan(n-2)
    else:
        return 0
N = int(input("Masukkan hari ke-N(bilangan bulat positif): "))
hasil = hitung_pelanggan(N)
print(f"Jumlah pelanggan pada hari ke-{N} adalah: {hasil}")
