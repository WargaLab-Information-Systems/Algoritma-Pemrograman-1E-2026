buku = 3 * 25000
pulpen = 2 * 8000
flashdisk = 1 * 75000

total = buku + pulpen + flashdisk
diskon = total * 0.10
setelahDiskon = total - diskon
pajak = setelahDiskon * 0.11
bayar = setelahDiskon + pajak
kembalian = 200000 - bayar

print("Harga buku =", buku)
print("Harga pulpen =", pulpen)
print("Harga flashdisk =", flashdisk)
print("Total belanja =", total)
print("Diskon =", diskon)
print("Setelah diskon =", setelahDiskon)
print("Pajak =", pajak)
print("Total bayar =", bayar)
print("Kembalian =", kembalian)