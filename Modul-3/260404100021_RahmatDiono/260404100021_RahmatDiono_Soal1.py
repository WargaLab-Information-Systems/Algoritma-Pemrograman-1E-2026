penumpang = 0
total_jarak = 0
total_pendapatan = 0
jarak_terjauh = 0

while True:
    jarak = int(input("Masukkan jarak: "))
    if jarak == 0:
        break
    if jarak < 0:
        print("Masukkan nilai valid")
        continue
    penumpang += 1
    total_jarak += jarak

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    if penumpang % 5 == 0:
        tarif = tarif * 0.5
        print("Diskon 50%")
    total_pendapatan += tarif

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak
if penumpang > 0:
    rerata = total_jarak / penumpang
else:
    rerata = 0

print("\nJumlah penumpang:", penumpang, "orang")
print("Total pendapatan: Rp", total_pendapatan)
print("Jarak terjauh:", jarak_terjauh, "km")
print("Rata-rata jarak:", rerata, "km")