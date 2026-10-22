jumlah_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
total_jarak = 0

while True:
    jarak = int(input("Masukkan jarak penumpang (km), 0 for selesai: "))
    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid! Harap masukkan jarak yang benar.")
        continue
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    jumlah_penumpang += 1
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 50 // 100
        print("Penumpang ke-",jumlah_penumpang, "mendapat diskon 50%!")

    total_pendapatan += tarif
    total_jarak += jarak

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

    print(f"Penumpang ke-{jumlah_penumpang} Jarak: {jarak} km Tarif: Rp{tarif:,}")
print("\n=== Ringkasan Akhir ===")
print("Jumlah penumpang:", jumlah_penumpang, "orang")
print("Total pendapatan: Rp", total_pendapatan)
print("Jarak terjauh:",jarak_terjauh, "km")

if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang
    print("Rata-rata jarak:", rata_rata, "km")
else:
    print("Rata-rata jarak   : 0 km (tidak ada penumpang)")
