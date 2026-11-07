def fibbonanci(n):
    if n == 1 or n == 2:
       return 1
    else :
        return fibbonanci(n-1) + fibbonanci(n-2)

n = int(input("Masukkan Hari Ke : "))
hasil = fibbonanci(n)
print("Jumlah Pelanggan :", hasil, "orang")