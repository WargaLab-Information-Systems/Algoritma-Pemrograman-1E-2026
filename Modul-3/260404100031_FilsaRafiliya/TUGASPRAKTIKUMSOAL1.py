jumlahPenumpang = 0
totalPendapatan = 0
jarakTerjauh = 0
totalJarak = 0

jarak = float(input("berapa jaraknya: "))
jarak1 = 3000

tarif = 0

while jarak != 0:
    if jarak <0:
        print ("jarak tidak valid, silahkan ulangi")
        continue
    jumlahPenumpang += 1

    if jarak <= 5:
        tarif = jarak1
        print ("dikenakan harga", jarak1)
    elif jarak >5 and jarak <=15:
        tarif = jarak1 + 1000 * (jarak - 5)
        print ("dikenakan harga", tarif)
    else:
        tarif = 13000 + 500 * (jarak - 15)
        print ("dikenakan harga", tarif)

    if jumlahPenumpang % 5 == 0:
        print ("mendapatkan diskon sebesar 50%, hingga bayarannya hanya menjadi", tarif - (tarif * 0.50))

    
    totalPendapatan += tarif
    totalJarak += jarak
    if jarak > jarakTerjauh:
        jarakTerjauh = jarak

    jarak = float(input("masukkan jarak: "))

#hasil 
print ("total pendapatannya adalah", totalPendapatan)
print ("total jarak yang ditempuh adalah", totalJarak)
print ("jarak terjauhnya dalah", jarakTerjauh)
print ("jumlah penumpangnya adalah", jumlahPenumpang)

rata2Jarak = (totalJarak / jumlahPenumpang)
print ("rata-rata jarak yang ditempuh adalah", rata2Jarak)

