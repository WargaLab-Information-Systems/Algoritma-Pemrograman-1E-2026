jumlah_penuh = 0

for i in range(1, 11):
    print("Mahasiswa ke-", i)

    nama = input("Nama: ")
    ipk = float(input("IPK: "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat.")
        continue

    penghasilan = int(input("Penghasilan orang tua per bulan: "))

    if penghasilan <= 3000000:
        print(nama, "mendapat beasiswa penuh.")
        jumlah_penuh += 1

    elif penghasilan <= 5000000:
        print(nama, "mendapat beasiswa sebagian.")

    else:
        print(nama, "tidak mendapat beasiswa.")

    if jumlah_penuh == 3:
        print("Kuota beasiswa penuh sudah terpenuhi.")
        break

print("Jumlah penerima beasiswa penuh:", jumlah_penuh)
