def nilai_mahasiswa(nama, tugas, uts, uas):
    # Menghitung nilai akhir
    akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)
    # Menentukan grade
    if akhir >= 85:
        grade = "A" 
    elif akhir >= 70:
        grade = "B"
    elif akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    # Menentukan status kelulusan
    if grade == "A" or grade == "B" or grade == "C":
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    # Menampilkan hasil
    print("Nama Mahasiswa :", nama)
    print("Nilai Tugas    :", tugas)
    print("Nilai UTS      :", uts)
    print("Nilai UAS      :", uas)
    print("Nilai Akhir    :", akhir)
    print("Grade          :", grade)
    print("Status         :", status)

# Input data mahasiswa
nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))
if tugas or uts or uas > 100:
    print("ga bisa woy nilainya lebih dari 100")
else:
# Memanggil function
    nilai_mahasiswa(nama, tugas, uts, uas)