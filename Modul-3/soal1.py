jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0
while True:
    jarak = int(input("masukkan jarak penumpang (km):  "))
    if jarak == 0:
        break
    if jarak < 0:
        print("jarak tidak valid, coba masukkan ulang.")
        continue
    jumlah_penumpang = jumlah_penumpang + 1
    if jarak <= 5 :
        tarif = 3000
    elif jarak <= 15:
        tarif= 3000 + ( jarak - 5) * 1000
    else:
        tarif= 13000 + (jarak - 15) * 500
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print("yey, anda dapat diskon 50 persen ")
        print("tarif penumpang :  Rp", tarif)  
    total_pendapatan = total_pendapatan + tarif
    total_jarak = total_jarak + jarak 
    if jarak > jarak_terjauh: 
            jarak_terjauh = jarak
print("Jumlah penumpang:  ", jumlah_penumpang)
print("total pendapatan:  ", total_pendapatan, "Rp")
if jumlah_penumpang > 0 :
    rata_rata = total_jarak / jumlah_penumpang
    print("jarak terjauh: ", jarak_terjauh, "KM")
    print("Rata-rata jarak: ", rata_rata, "KM")
else:
    print("Jarak terjauh: 0 KM")
    print('Rata-rata jarak: 0 KM')   
