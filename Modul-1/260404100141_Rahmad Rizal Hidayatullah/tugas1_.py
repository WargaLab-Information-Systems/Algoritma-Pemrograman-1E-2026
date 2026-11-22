buku = 3 * 25000
pulpen = 2 * 8000
flashdisk = 1 * 75000

total_belanja = buku + pulpen + flashdisk

diskon = total_belanja * 10 / 100
harga_diskon = total_belanja - diskon
ppn = harga_diskon * 11 / 100
total_bayar = harga_diskon + ppn
uang_udIn = 2 * 100000
kembalian = uang_udIn - total_bayar
print("===== STRUK BELANJA UDIN =====")
print("Total harga buku       : Rp", buku)
print("Total harga pulpen     : Rp", pulpen)
print("Total harga flashdisk  : Rp", flashdisk)
print("Total sebelum diskon   : Rp", total_belanja)
print("Diskon 10%              : Rp", diskon)
print("Harga setelah diskon   : Rp", harga_diskon)
print("PPN 11%                 : Rp", ppn)
print("Total pembayaran       : Rp", total_bayar)
print("Uang tunai              : Rp", uang_udIn)
print("Uang kembalian          : Rp", kembalian)
