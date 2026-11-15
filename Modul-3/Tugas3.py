jumlah_mahasiswa = 10 

jumlah_a = 0
jumlah_b = 0
jumlah_c = 0
jumlah_d = 0
jumlah_e = 0
total_nilai_akhir = 0

nilai_tertinggi = -1
nama_tertinggi = "" 
nilai_terendah = 101
nama_terendah = ""
print("=== program pengelolaan nilai mahasiswa ===")
for i in range(1, jumlah_mahasiswa + 1):
    print(f"\nmahasiswa ke -{i}")
    nama = input("Masukkan Nama: ")
    nilai_tugas = float(input("Nilai Tugas (0-100): "))
    nilai_uts = float(input("Nilai UTS (0-100): "))
    nilai_uas = float(input("Nilai UAS (0-100): "))
    nilai_akhir = (nilai_tugas * 0.3) +(nilai_uts * 0.3) + ( nilai_uas * 0.4)

    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_a += 1
    elif nilai_akhir >=75:
        kategori = "B"
        jumlah_b += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_c += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_d += 1
    else:
        kategori = "E"
        jumlah_e += 1
    
    total_nilai_akhir += nilai_akhir

    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama

    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama
    print(f"-> nilai akhir: {nilai_akhir:.2f} | kategori: {kategori}")

rata_rata_kelas = total_nilai_akhir / jumlah_mahasiswa

print("\n=== REKAPITULASI KELAS ===")
print(f"jumlah kategori a : {jumlah_a}")
print(f"jumlah kategori b : {jumlah_b}")
print(f"jumlah kategori c : {jumlah_c}")
print(f"jumlah kategori d : {jumlah_d}")
print(f"jumlah kategori e : {jumlah_e}")
print(f"nilai tertinggi : {nilai_tertinggi:.2f} (oleh{nama_tertinggi})")
print(f"nilai terendah : {nilai_terendah:.2f} (oleh{nama_terendah})")
print(f"rata-rata kelas : {rata_rata_kelas:.2f} (oleh{nama_tertinggi})")