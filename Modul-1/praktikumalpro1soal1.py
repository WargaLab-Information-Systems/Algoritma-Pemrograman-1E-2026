#belanja udin 
buku = 25.000
pulpen = 8.000
flashdisk = 75.000

#jumlah harga 
jumlahBuku = (buku * 3)
print ("total harga bukunya adalah", jumlahBuku)
jumlahPulpen = (pulpen * 2)
print ("total harga pulpen adalah", jumlahPulpen )

#total harga 
totalHarga = (jumlahBuku + jumlahPulpen + flashdisk)
print ("total  harga keseluruhan adalah", totalHarga)

#harga setelah diskon 
diskon = (totalHarga * 0.10)
harga_setelah_diskon = (totalHarga - diskon)
print ("dikarenakan ini adalah awal semester udin mendapatkan diskon sebsera 10%, sehingga total barangnya menjadi", harga_setelah_diskon)

#dikenakan pajak sebesar 11%
pajak = (harga_setelah_diskon * 0.11)
hargaDibayar = (harga_setelah_diskon + pajak)
print ("transaksi udin dikenakan pajak sebesar 11%, jadi total pembayaran yang harus dibayar oleh udin adalah", hargaDibayar)

#pembayaran 
#udin membayar dengan uang sebesar 200.000
kembalianUdin = (200.000 - hargaDibayar)
print ("udin membayar dengan uang sebesar 200.000, maka udin mendapat kembalian sebesar", kembalianUdin)


