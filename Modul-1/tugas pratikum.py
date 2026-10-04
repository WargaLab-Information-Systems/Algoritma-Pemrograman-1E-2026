#SOAL 1

# Input data barang
jumlah_buku = 3
harga_buku = 25000

jumlah_pulpen = 2
harga_pulpen = 8000

jumlah_flashdisk = 1
harga_flashdisk = 75000

uang_udIN = 2 * 100000

# a) Total harga buku
total_buku = jumlah_buku * harga_buku

# b) Total harga pulpen
total_pulpen = jumlah_pulpen * harga_pulpen

# c) Total harga flashdisk
total_flashdisk = jumlah_flashdisk * harga_flashdisk

# d) Total harga seluruh barang sebelum diskon
total_awal = total_buku + total_pulpen + total_flashdisk

# e) Besarnya diskon 10%
diskon = total_awal * 10 / 100

# f) Harga barang setelah diskon
harga_setelah_diskon = total_awal - diskon

# g) Besarnya pajak 11%
pajak = harga_setelah_diskon * 11 / 100

# h) Total pembayaran setelah pajak
total_pembayaran = harga_setelah_diskon + pajak

# i) Uang kembalian
kembalian = uang_udIN - total_pembayaran

# Menampilkan hasil
print("Total harga buku       : Rp", total_buku)
print("Total harga pulpen     : Rp", total_pulpen)
print("Total harga flashdisk  : Rp", total_flashdisk)
print("Total sebelum diskon   : Rp", total_awal)
print("Diskon 10%             : Rp", diskon)
print("Harga setelah diskon   : Rp", harga_setelah_diskon)
print("Pajak 11%              : Rp", pajak)
print("Total pembayaran       : Rp", total_pembayaran)
print("Uang kembalian         : Rp", kembalian)

#SOAL NO 2
r = float(input("Masukkan Jari-jari nya ="))
t = float(input("Masukkan Tinggi nya ="))

phi = 3.13
volume_kerucut = 1 / 3 * (phi * r * r * t)
print("Volume kerucut =" , volume_kerucut , 'CM')


#SOAL 3
jarak_pergi = 100
jarak_pulang = 100
konsumsi_bahan_bakar = 40
sisa_bahan_bakar = 1.5
harga_bahan_bakar = 10000

total_jarak = jarak_pergi + jarak_pulang
kebutuhan_bahan_bakar = total_jarak / konsumsi_bahan_bakar
bahan_bakar_dibeli = kebutuhan_bahan_bakar - sisa_bahan_bakar
total_biaya = bahan_bakar_dibeli * harga_bahan_bakar

print("Total jarak perjalanan       :", total_jarak, "km")
print("Total kebutuhan bahan bakar  :", kebutuhan_bahan_bakar, "liter")
print("Bahan bakar yang dibeli      :", bahan_bakar_dibeli, "liter")
print("Total biaya bahan bakar      : Rp", total_biaya)