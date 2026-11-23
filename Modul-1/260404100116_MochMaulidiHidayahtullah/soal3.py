
jarak = 100
bensin = 40
sisa = 1.5
harga = 10000

total_jarak = jarak * 2
total_bensin = total_jarak / bensin
beli = total_bensin - sisa
biaya = beli * harga

print("Jarak PP:", total_jarak, "KM")
print("Kebutuhan bensin:", total_bensin, "L")
print("Bensin dibeli:", beli, "L")
print("Total biaya: Rp", biaya)


