jumlah_mahasiswa = 10 
kuota_beasiswa_penuh = 3
penerima_penuh = 0
print("=== Program Seleksi Beasiswa Mahasiswa ===")
for i in range(1, jumlah_mahasiswa + 1):
    print(f"\n--- mahasiswa ke-{i} ---")
    nama = input("Masukkan Nama Mahasiswa: ")
    ipk = float(input("Masukkan IPK (skala 0.0 - 4.0): "))
    if ipk < 3.00:
        print(f"Status: {nama} tidak memenuhi syarat (IPK < 3.00). proses dilewati.")
        continue
    penghasilan = float(input("Masukkan penghasilan orang tua per bulan (Rp): "))
    if penghasilan <= 3000000:
        penerima_penuh += 1
        print(f"Status: {nama} Mendapatkan Beasiswa Penuh")
        if penerima_penuh >= kuota_beasiswa_penuh:
            print("\n[INFO] kuota beasiswa penuh (3 orang) telah terpenuhi!")
            print("proses seleksi dihentikan lebih awal")
            break
    elif penghasilan <= 5000000:
        print(f"Status: {nama} mendapatkan beasiswa sebagian")
    else:
        print(f"Status: {nama} tidak menerima beasiswa (penghasilan > Rp.5.000.000)")
print("\n=== Proses Seleksi Selesai ===")
print(f"total mahasiswa yang mendapatkan beasiswa penuh sejauh ini {penerima_penuh}")
