jumlah = 0
total = 0
total_jarak = 0
terjauh = 0

jarak = float(input("Masukkan jarak penumpang (0 untuk selesai): "))

while jarak != 0:
    if jarak < 0:
        print("Jarak tidak valid!")
    else:
        jumlah = jumlah + 1
        total_jarak = total_jarak + jarak

        if jarak > terjauh:
            terjauh = jarak

        if jarak <= 5:
            tarif = 3000
        elif jarak <= 15:
            tarif = 3000 + (jarak - 5) * 1000
        else:
            tarif = 13000 + (jarak - 15) * 500

        if jumlah % 5 == 0:
            tarif = tarif * 0.5
            print("Diskon 50%")

        total = total + tarif
        print("Tarif penumpang: Rp", tarif)

    jarak = float(input("Masukkan jarak penumpang (0 untuk selesai): "))

print("\nJumlah penumpang:", jumlah)
print("Total pendapatan: Rp", total)
print("Jarak terjauh:", terjauh, "km")

if jumlah > 0:
    rata = total_jarak / jumlah
else:
    rata = 0

print("Rata-rata jarak:", rata, "km")
