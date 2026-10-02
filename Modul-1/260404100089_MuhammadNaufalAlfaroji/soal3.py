jarak_tempuh = 100
konsumsi_motor = 40 
bensin_awal = 1.5
harga_bensin = 10000

total_jarak = jarak_tempuh * 2
total_bensin= total_jarak / konsumsi_motor
total_dibeli = total_bensin - bensin_awal
total_biaya = total_dibeli * harga_bensin

print("jarak tempuh:", total_jarak, "km")
print("kebutuhan bensin:", total_bensin, "liter")
print("bensin yg harus dibeli:", total_dibeli, "liter")
print("total biaya bensin;", total_biaya, "ribu")
