uang_udin = 2 * 100000
print("Uang yang dibawa Udin: Rp", uang_udin)

buku = 3
harga_buku_satu = 25000
total_buku = buku * harga_buku_satu
print("a) Total harga buku: Rp", total_buku)

pulpen = 2
harga_pulpen_satu = 8000
total_pulpen = pulpen * harga_pulpen_satu
print("b) Total harga pulpen: Rp", total_pulpen)

flashdisk = 1
harga_flashdisk_satu = 75000
total_flashdisk = flashdisk * harga_flashdisk_satu
print("c) Total harga Flashdisk: Rp", total_flashdisk)

total_semua_barang = total_buku + total_pulpen + total_flashdisk
print("d) Total harga seluruh barang sebelum diskon: Rp", total_semua_barang)

besar_diskon = total_semua_barang * 10 / 100
print("e) Besarnya diskon 10%: Rp", besar_diskon)

harga_setelah_diskon = total_semua_barang - besar_diskon
print("f) Harga barang setelah diskon: Rp", harga_setelah_diskon)

besar_pajak = harga_setelah_diskon * 11 / 100
print("g) Besarnya pajak 11%: Rp", besar_pajak)

total_akhir_bayar = harga_setelah_diskon + besar_pajak
print("h) Total pembayaran setelah pajak: Rp", total_akhir_bayar)

uang_kembalian = uang_udin - total_akhir_bayar
print("i) Uang kembalian yang diterima Udin: Rp", uang_kembalian)
