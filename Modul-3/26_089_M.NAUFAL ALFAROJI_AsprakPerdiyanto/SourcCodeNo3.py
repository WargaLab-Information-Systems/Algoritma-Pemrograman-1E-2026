
jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0
total_nilai = 0
nilai_tertinggi = -1
nilai_terendah = 101
nama_tertinggi = ""
nama_terendah = ""

for i in range(1, 11):
    print(f"\nMahasiswa ke-{i}")

    nama = input("Nama mahasiswa: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    total_nilai += nilai_akhir

    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama

    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

    print(f"Nilai akhir: {nilai_akhir:.2f}")
    print(f"Kategori: {kategori}")

print("= REKAP NILAI =")
print(f"Kategori A: {jumlah_A} mahasiswa")
print(f"Kategori B: {jumlah_B} mahasiswa")
print(f"Kategori C: {jumlah_C} mahasiswa")
print(f"Kategori D: {jumlah_D} mahasiswa")
print(f"Kategori E: {jumlah_E} mahasiswa")

print(f"Nilai tertinggi: {nilai_tertinggi:.2f}")
print(f"Mahasiswa: {nama_tertinggi}")

print(f"Nilai terendah: {nilai_terendah:.2f}")
print(f"Mahasiswa: {nama_terendah}")

rata_rata = total_nilai / 10
print(f"Rata-rata kelas: {rata_rata:.2f}")