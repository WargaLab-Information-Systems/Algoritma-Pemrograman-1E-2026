total_belanja_awal = float(input("masukkan total belanja awal (Rp): "))
diskon_persen = 0 
total_bayar = 0

if total_belanja_awal % 100000 == 0:
    diskon_persen = 100
    total_bayar = 0
elif total_belanja_awal % 50000 == 0:
    diskon_persen = 50
    total_bayar = total_belanja_awal * 0.5
elif total_belanja_awal % 10000 == 0:
    diskon_persen = 20 
    total_bayar = total_belanja_awal * 0.8
elif total_belanja_awal >=200000:
    diskon_persen = 10 
    total_bayar = total_belanja_awal * 0.9
else:
    diskon_persen = 0
    total_bayar = total_belanja_awal

Status_poin = "poin bertambah" if total_bayar > 0 else "tidak ada poin"

print("\n" + "="*30)
print("RINCIAN BELANJA SITI")
print("="*30)
print(f"Total Belanja Awal : Rp {total_belanja_awal:,.2f}")
print(f"Diskon Didapat : {diskon_persen}%")
print(f"Total Harga Akhir : Rp {total_bayar:,.2f}")
print(f"Status Poin : {Status_poin}")
print("=" * 40)
