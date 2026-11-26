def kelulusan (nilaiAkhir):
    nilaiAkhir = (nilaiTugas * 0.30) + (nilaiUTS * 0.30) + (nilaiUAS * 0.40)
    if nilaiAkhir >= 85:
        grade = "A"
    elif nilaiAkhir >= 70 and nilaiAkhir <85:
        grade = "B"
    elif nilaiAkhir >=55 and nilaiAkhir <75:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    print("Nama Mahasiswa   :", nama)
    print("Nilai Akhir      :", nilaiAkhir)
    print("Grade            :", grade)
    print("Status           :", status)

nama =  input("masukkan nama mahasiswa: ")
nilaiTugas = int(input("masukkan nilai tugas: "))
nilaiUTS = int(input("masukkan nilai UTS: "))
nilaiUAS = int(input("masukkan nilai UAS: "))
nilaiAkhir = (nilaiTugas * 0.30) + (nilaiUTS * 0.30) + (nilaiUAS * 0.40)

kelulusan(nilaiAkhir)
