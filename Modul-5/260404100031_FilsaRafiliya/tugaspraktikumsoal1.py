def pelanggan (hari):
    if hari == 1 or hari == 2:
        return 1
    return pelanggan (hari-1) + pelanggan (hari-2)

N = int(input("masukkan hari ke-N: "))
print (f"Jumlah pelanggan pada hari ke-{N} adalah {pelanggan(N)} orang")