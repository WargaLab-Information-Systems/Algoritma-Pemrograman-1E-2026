jumlah_penumpang = 0
total_pendapatan = 0 
jarak_terjauh = 0
total_jarak = 0

print("=== program Perhitungan Tarif Bus Sidoarjo ===")
print("Masukan jarak tempuh penumpang (masukan 0 untuk berhenti).\n")

while True:
    jarak = float(input("masukkan jarak tempuh(km)"))

    if jarak == 0:
        break
    if jarak < 0:
        print("jarak tidak valid! silakan masukkan angka positif.")
        continue
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    jumlah_penumpang += 1
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print(f"-> penumpang ke {jumlah_penumpang} mendapatkan diskon 50%!")

    total_pendapatan += tarif
    total_jarak += jarak 
    if jarak > jarak_terjauh:
        jarak_terjauh = jarak
if jumlah_penumpang >0:
    rata_rata_jarak = total_jarak / jumlah_penumpang
else:
     rata_rata_jarak = 0

print("\n=== laporan akhir terminal bus ===")
print(f"jumlah penumpang valid : {jumlah_penumpang}")
print(f"total pendapatan : Rp {total_pendapatan:,.0f}")
print(f"jarak terjauh : {jarak_terjauh}km")
print(f"Rata-rata jarak : {rata_rata_jarak:.2f} km")
