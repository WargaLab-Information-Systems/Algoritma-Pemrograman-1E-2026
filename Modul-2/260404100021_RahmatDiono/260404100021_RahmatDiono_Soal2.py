#KOPERASI NDESO ABANG PUTEH
belanja = float(input("Masukan harga belanja: "))

if belanja % 100000 == 0:
    total_belanja = 0
    print("Belanjaan gratis")
elif belanja % 50000 == 0:
    total_belanja = belanja * 50 // 100
    print(f"Total belanja: Rp{total_belanja}")

elif belanja % 10000 == 0:
    total_belanja = belanja * 80 // 100
    print(f"Total belanja: Rp{total_belanja}")

elif belanja >= 200000:
    total_belanja = belanja * 90 // 100
    print(f"Total belanja: Rp{total_belanja}")
    
else:
    total_belanja = belanja
    print(f"Total belanja: Rp{total_belanja}")

print("Total harga belanjaan siti : Rp", total_belanja)

status_poin = "Poin bertambah" if total_belanja > 0 else "Tidak ada poin"

print(status_poin)