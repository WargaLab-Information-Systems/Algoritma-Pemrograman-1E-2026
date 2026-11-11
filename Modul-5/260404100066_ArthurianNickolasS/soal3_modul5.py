def nilai_mahasiswa(nama, tugas, uts, uas):
    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)
    return nilai_akhir

nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = nilai_mahasiswa(nama, tugas, uts, uas)
print(f"Nilai akhir {nama}: {nilai_akhir}")

def kategori_nilai(n):
    if n >= 85:
        return "A"
    elif n >= 70:
        return "B"
    elif n >= 55:
        return "C"
    else:
        return "E"
print("Kategori nilai:", kategori_nilai(nilai_akhir ))