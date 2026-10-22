nomor_mahasiswa = 1
jumlah_beasiswa_penuh = 0

while nomor_mahasiswa <= 10:
    print("Mahasiswa ke-", nomor_mahasiswa)
    nama = input("Masukkan nama mahasiswa: ")
    ipk = float(input("Masukkan IPK: "))
    if ipk < 3.00:
        print("Hasil: Tidak memenuhi syarat karena IPK kurang dari 3,00")
        nomor_mahasiswa = nomor_mahasiswa + 1
        continue
    penghasilan_orang_tua = int(
        input("Masukkan penghasilan orang tua per bulan: Rp"))
    if penghasilan_orang_tua <= 3000000:
        hasil = "Beasiswa penuh"
        jumlah_beasiswa_penuh = jumlah_beasiswa_penuh + 1
    elif penghasilan_orang_tua <= 5000000:
        hasil = "Beasiswa sebagian"
    else:
        hasil = "Tidak mendapat beasiswa"
    print("Nama:", nama)
    print("IPK:", ipk)
    print("Penghasilan orang tua: Rp", penghasilan_orang_tua)
    print("Hasil seleksi:", hasil)
    if jumlah_beasiswa_penuh == 3:
        print("Kuota beasiswa penuh sudah terpenuhi.")
        break
    nomor_mahasiswa = nomor_mahasiswa + 1
print("Seleksi selesai.")
print("Jumlah mahasiswa yang diproses:", nomor_mahasiswa)
print("Jumlah penerima beasiswa penuh:", jumlah_beasiswa_penuh)