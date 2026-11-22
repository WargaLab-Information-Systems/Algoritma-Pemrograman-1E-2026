# --- 1. KURSI BEASISWA PENUH YANG SUDAH TERISI (AWALNYA 0) ---
jumlah_penuh = 0

# --- 2. PANGGIL ANTREAN MAKSIMAL 10 MAHASISWA (1 SAMPAI 10) ---
for i in range(1, 11):
    print("--- Mahasiswa ke-%d ---" % i)
    nama = input("Nama                  : ")
    ipk = float(input("IPK                   : "))  # Pake float karena nilainya desimal/koma
    penghasilan = int(input("Penghasilan ortu/bulan: "))

    # Syarat Wajib 1: IPK minimal harus 3.00
    if ipk < 3.00:
        print(">> %s: IPK < 3.00, dilewati" % nama)
        continue  # SKIP orang ini! Langsung panggil antrean berikutnya

    # Kalau IPK lolos, cek kemampuan ekonomi orang tua
    if penghasilan <= 3000000:
        print(">> %s: BEASISWA PENUH" % nama)
        jumlah_penuh += 1  # 1 kursi beasiswa penuh terisi
    elif penghasilan <= 5000000:
        print(">> %s: BEASISWA SEBAGIAN" % nama)
    else:
        print(">> %s: TIDAK dapat beasiswa" % nama)

    # Syarat Kuota: Kursi beasiswa penuh cuma ada 3!
    if jumlah_penuh == 3:
        print("Kuota penuh (3), seleksi dihentikan!")
        break  # STOP antrean sekarang juga, loket pendaftaran ditutup!

# --- 3. LAPORAN AKHIR TOTAL PENERIMA ---
print("Total beasiswa penuh:", jumlah_penuh)
