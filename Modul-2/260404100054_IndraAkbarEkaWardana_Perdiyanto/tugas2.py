belanja = int(input("Masukkan total belanja: Rp"))

print("Total belanja awal : Rp", belanja)

if belanja % 100000 == 0:
    bayar = 0
    print("Diskon 100% - Belanja Gratis")

elif belanja % 50000 == 0:
    bayar = belanja - (belanja * 50 // 100)
    print("Diskon 50%")

elif belanja % 10000 == 0:
    bayar = belanja - (belanja * 20 // 100)
    print("Diskon 20%")

elif belanja >= 200000:
    bayar = belanja - (belanja * 10 // 100)
    print("Diskon 10%")

else:
    bayar = belanja
    print("Tidak mendapatkan diskon")

print("Total harga akhir : Rp", bayar)

poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"

print("Status poin :", poin)
