n = int(input("Masukkan tinggi setengah menara(n, valid 2 sampai 15): "))
while n < 2 or n > 15:
    print("Nilai n harus di antara 2 sampai 15. Silakan ulangi!")
    n = int(input("Masukkan tinggi setengah menara(n, valid 2 sampai 15):"))

for i in range(1, n + 1):
    barisan = ""
    for j in range(1, i + 1):
        angka = j % 10
        barisan += str(angka)
        
    for j in range(i - 1, 0, -1):
        angka = j % 10 
        barisan += str(angka)

    print(barisan.center(n * 2 - 1))

for i in range(n - 1, 0, -1):
    barisan = "" 
    for j in range(1, i + 1 ):
            angka = j % 10 
            barisan += str(angka)
    for j in range(i - 1, 0, -1):
            angka = j % 10
            barisan += str(angka)
            
    print(barisan.center(n * 2 -1))
