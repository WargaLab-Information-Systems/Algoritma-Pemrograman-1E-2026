# --- 1. SIAPKAN TOPLES PENCATAT (WADAH AWAL) ---
jumlah_penumpang = 0  # Wadah hitung berapa orang yang naik bus
total_pendapatan = 0  # Wadah total uang yang terkumpul
jarak_terjauh = 0     # Catatan rekor jarak paling jauh
total_jarak = 0       # Wadah total seluruh kilometer perjalanan

# --- 2. MULAI TANYA PENUMPANG SATU PER SATU (MUTER TERUS) ---
while True:
    # Minta input jarak dari penumpang
    jarak = int(input("Jarak penumpang (km, 0 = selesai): "))

    # Kalau diketik 0, artinya bus sudah sampai terminal, STOP!
    if jarak == 0:
        break

    # Kalau jaraknya minus (tidak masuk akal), tegur dan ulangi tanya
    if jarak < 0:
        print("Jarak negatif tidak valid, ulangi!")
        continue  # Lewati baris di bawah, langsung ulangi tanya

    # Catat 1 penumpang baru masuk
    jumlah_penumpang += 1

    # --- 3. HITUNG HARGA TIKET BERDASARKAN JARAK ---
    if jarak <= 5:
        # Dekat (1-5 km) bayar flat Rp 3.000
        tarif = 3000
    elif jarak <= 15:
        # Sedang (6-15 km): Rp 3.000 + Rp 1.000 per km kelebihannya
        tarif = 3000 + (jarak - 5) * 1000
    else:
        # Jauh (> 15 km): Rp 13.000 + Rp 500 per km kelebihannya
        tarif = 13000 + (jarak - 15) * 500

    # --- 4. PROMO DISKON KELIPATAN 5 ---
    # Jika penumpang urutan ke-5, ke-10, dst. (% 5 sisa 0 artinya kelipatan 5)
    if jumlah_penumpang % 5 == 0:
        tarif = tarif // 2  # Diskon 50% (dibagi 2 buang koma)
        print("Penumpang ke-%d diskon 50%%" % jumlah_penumpang)

    # Cetak karcis tarif untuk penumpang ini
    print("Tarif penumpang ke-%d: Rp%d" % (jumlah_penumpang, tarif))

    # Masukkan uang tarif ke total dan tambahkan jarak ke total jarak
    total_pendapatan += tarif
    total_jarak += jarak

    # Cek apakah jarak penumpang ini memecahkan rekor jarak terjauh
    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

# --- 5. CETAK REKAP LAPORAN AKHIR ---
print("=== REKAP ===")
print("Jumlah penumpang :", jumlah_penumpang)
print("Total pendapatan : Rp%d" % total_pendapatan)
print("Jarak terjauh    :", jarak_terjauh, "km")

# Hitung rata-rata jarak (cegah error bagi 0 kalau tidak ada penumpang)
if jumlah_penumpang > 0:
    print("Rata-rata jarak  : %.2f km" % (total_jarak / jumlah_penumpang))
else:
    print("Rata-rata jarak  : 0 km")
