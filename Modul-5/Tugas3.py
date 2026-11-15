def hitung_nilai(nama, tugas, uts, uas):
    nilai = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    if nilai >= 85:
        grade = "A"
    elif nilai >= 70:
        grade = "B"
    elif nilai >= 55:
        grade = "C"
    else:
        grade = "D"

    status = "Lulus" if grade in ("A", "B", "C") else "Tidak Lulus"

    print("\n=== HASIL PERHITUNGAN ===")
    print(f"Nama Mahasiswa : {nama}")
    print(f"Nilai Tugas    : {tugas}")
    print(f"Nilai UTS      : {uts}")
    print(f"Nilai UAS      : {uas}")
    print(f"Nilai Akhir    : {nilai:.2f}")
    print(f"Grade          : {grade}")
    print(f"Status         : {status}")

nama = input("Nama mahasiswa: ")
tugas = float(input("tugas: "))
uts = float(input("uts: "))
uas = float(input("uas: "))

hitung_nilai(nama, tugas, uts, uas)