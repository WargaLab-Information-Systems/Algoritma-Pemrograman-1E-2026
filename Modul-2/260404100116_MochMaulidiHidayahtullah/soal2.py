belanja = int(input("Masukkan total belanja: Rp"))

if belanja % 100000 == 0:
    bayar = 0
elif belanja % 50000 == 0:
    bayar = belanja - (belanja * 50 // 100)
elif belanja % 10000 == 0:
    bayar = belanja - (belanja * 20 // 100)
elif belanja >= 200000:
    bayar = belanja - (belanja * 10 // 100)
else:
    bayar = belanja

poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"

print("Total belanja awal: Rp", belanja)
print("Total yang harus dibayar: Rp", bayar)
print("Status poin:", poin)
