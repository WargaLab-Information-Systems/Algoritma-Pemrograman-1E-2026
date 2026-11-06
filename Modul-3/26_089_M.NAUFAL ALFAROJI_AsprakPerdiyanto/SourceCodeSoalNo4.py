
jumlah_beasiswa_penuh = 0

for i in range(1, 11):
    print(f"\nData Mahasiswa ke-{i}")

    nama = input("Masukkan nama mahasiswa: ")
    ipk = float(input("Masukkan IPK: "))
    penghasilan = int(input("Masukkan penghasilan orang tua per bulan: Rp"))

    if ipk < 3.00:
        print(f"{nama} tidak memenuhi syarat beasiswa karena IPK kurang dari 3,00.")
        continue

    if penghasilan <= 3000000:
        print(f"{nama} mendapatkan beasiswa penuh.")
        jumlah_beasiswa_penuh += 1

    elif penghasilan <= 5000000:
        print(f"{nama} mendapatkan beasiswa sebagian.")

    else:
        print(f"{nama} tidak mendapatkan beasiswa karena penghasilan orang tua terlalu tinggi.")

    if jumlah_beasiswa_penuh == 3:
        print("\nKuota beasiswa penuh telah terpenuhi.")
        print("Proses seleksi dihentikan.")
        break

print(f"\nJumlah penerima beasiswa penuh: {jumlah_beasiswa_penuh}")
