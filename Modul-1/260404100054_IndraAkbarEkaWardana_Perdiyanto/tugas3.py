jarak = 100
irit = 40
sisa_bensin = 1.5
harga = 10000

jarak_pp = jarak * 2
butuh_bensin = jarak_pp / irit
beli_bensin = butuh_bensin - sisa_bensin
total_biaya = beli_bensin * harga

print("Total Jarak PP :", jarak_pp, "km")
print("Total Kebutuhan BBM Perjalanan :", butuh_bensin, "liter")
print("Sisa BBM di Tangki Awal :", sisa_bensin, "liter")
print("BBM yang Harus Dibeli di SPBU :", beli_bensin, "liter")
print("Total Biaya Pembelian BBM : Rp", total_biaya)
