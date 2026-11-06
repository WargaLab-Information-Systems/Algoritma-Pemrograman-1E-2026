
def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = tugas * 0.30 + uts * 0.30 + uas * 0.40
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"
        
    status = "Lulus" if grade != "D" else "Tidak Lulus"
    print(f"\nNama: {nama}")
    print(f"Nilai Akhir: {nilai_akhir:.2f}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")

nama = input("Nama mahasiswa: ")
tugas = float(input("Nilai tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))
hitung_nilai(nama, tugas, uts, uas)
