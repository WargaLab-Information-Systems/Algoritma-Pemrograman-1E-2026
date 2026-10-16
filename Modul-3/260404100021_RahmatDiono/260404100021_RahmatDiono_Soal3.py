jumlah = 0
nilai_A = 0
nilai_B = 0
nilai_C = 0
nilai_D = 0
nilai_E = 0

total = 0
tertinggi = -1
terendah = 101

for i in range(10):
    nama = input("Nama mahasiswa : ")
    if nama.lower() == "end":
        break

    tugas = int(input("Nilai tugas: "))
    uts = int(input("Nilai UTS: "))
    uas = int(input("Nilai UAS: "))

    akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4

    if akhir >= 85:
        kategori = "A"
        nilai_A += 1
    elif akhir >= 75:
        kategori = "B"
        nilai_B += 1
    elif akhir >= 65:
        kategori = "C"
        nilai_C += 1
    elif akhir >= 50:
        kategori = "D"
        nilai_D += 1
    else:
        kategori = "E"
        nilai_E += 1

    print(nama, tugas, uts, uas, round(akhir, 2), kategori)

    jumlah += 1
    total += akhir

    if akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama

    if akhir < terendah:
        terendah = akhir
        nama_terendah = nama

print("\n===== REKAPITULASI =====")
print("Jumlah mahasiswa:", jumlah)
print("Kategori A:", nilai_A)
print("Kategori B:", nilai_B)
print("Kategori C:", nilai_C)
print("Kategori D:", nilai_D)
print("Kategori E:", nilai_E)

if jumlah > 0:
    print("Nilai tertinggi:", tertinggi, "-", nama_tertinggi)
    print("Nilai terendah:", terendah, "-", nama_terendah)
    print("Rata-rata:", round(total / jumlah, 2))
else:
    print("Belum ada data mahasiswa.")