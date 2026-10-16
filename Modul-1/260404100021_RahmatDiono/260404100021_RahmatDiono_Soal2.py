jarak = 100     #km
sepeda = 40     #km/liter
sisa = 1.5      #liter
bensin = 10000  #Rp/liter

jarak_tempuh = jarak * 2
konsumsi_bbm = jarak_tempuh / sepeda
bbm_beli = konsumsi_bbm - sisa
total_biaya = bbm_beli * bensin
print("\n=== hasil perhitungan ====")
print(f"Total jarak tempuh : {jarak_tempuh} km")
print(f"Total kebutuhan BBM : {bbm_beli} liter")
print(f"Total biaya BBM : Rp{total_biaya}")
