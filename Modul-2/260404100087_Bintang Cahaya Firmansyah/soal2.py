total_belanja = int(input("Masukan total belanja: "))
if total_belanja % 100000 == 0:
    total_bayar = 0
elif total_belanja % 50000 == 0:
    total_bayar = total_belanja * 50 // 100
elif total_belanja % 10000 == 0:
    total_bayar = total_belanja * 80 // 100
elif total_belanja >= 200000:
    total_bayar = total_belanja * 90 // 100
else:
    total_bayar = total_belanja
print("Total belanja awal: Rp", total_belanja)
print("Total harga akhir: Rp", total_bayar)
if total_bayar > 0:
    print("poin bertambah")
else:
    print("poin tidak bertambah")
status_poin = total_bayar
print("Status Poin:", status_poin)