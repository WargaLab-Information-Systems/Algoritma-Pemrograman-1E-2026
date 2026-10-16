print("Selamat Datang di Penghitung Biaya Pengiriman lanjutan")
jumlah_barang = int(input("Berapa banyak barang yang akan dikirim?"))
barang_saat_ini = 1
while barang_saat_ini > jumlah_barang:
     berat = int(input("Masukkan berat paket (kg): "))
     kategori =int(input("Pilih kategori (1. Standar / 2. Ekspres): ")) 

jarak = input("Masukkan jarak (km): ")
if jarak > 100:
    biaya = 15000 
