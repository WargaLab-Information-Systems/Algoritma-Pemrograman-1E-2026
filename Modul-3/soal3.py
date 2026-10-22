jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0
total_nilai = 0
i = 1
while i <= 10:
    print("Mahasiswa ke-", i)
    nama = input("Nama mahasiswa:  ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS:  "))
    uas = float(input("Nilai UAS:  "))
    akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4
    total_nilai += akhir
    if akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1             
    print("Nama: ", nama)
    print("Nilai akhir: ", akhir) 
    print("Kategori:", kategori) 
    if i == 1:
        tertinggi = akhir
        terendah = akhir
        nama_tertinggi = nama
        nama_terendah = nama
    else:
        if akhir > tertinggi:
            tertinggi = akhir
            nama_tertinggi = nama
        if akhir < terendah:
            terendah = akhir
            nama_terendah = nama        
    i += 1 
rata_rata = total_nilai / 10
print("jumlah kategori A: ", jumlah_A)    
print("jumlah kategori B: ", jumlah_B)
print("jumlah kategori C: ", jumlah_C)
print("jumlah kategori D: ", jumlah_D)
print("jumlah kategori E: ", jumlah_E)
print("nilai tertinggi: ", tertinggi)
print("mahasiswa: ", nama_tertinggi)
print("nilai terendah: ", terendah)
print("mahasiswa: ", nama_terendah)
print("rata-rata kelas: ", rata_rata)