jumlah_penuh = 0

for i in range(1, 11):
    if jumlah_penuh == 3:
        break

    print("Mahasiswa ke-", i)

    nama = input("Masukkan nama: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print("Tidak memenuhi syarat beasiswa")
        continue
    else:
        penghasilan = float(input("Penghasilan orang tua: "))

        if penghasilan <= 3000000:
            print("Mendapat beasiswa penuh")
            jumlah_penuh = jumlah_penuh + 1
        elif penghasilan <= 5000000:
            print("Mendapat beasiswa sebagian")
        else:
            print("Tidak mendapat beasiswa")

    if jumlah_penuh == 3:
        print("Kuota beasiswa penuh sudah terpenuhi")
        break

print("Jumlah penerima beasiswa penuh:", jumlah_penuh)
print("Seleksi selesai")
