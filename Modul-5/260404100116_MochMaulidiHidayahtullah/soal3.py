# Fungsi menghitung nilai mahasiswa
def hitung_nilai(nama, tugas, uts, uas):
    nilai = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if nilai >= 85:
        grade = "A"
    elif nilai >= 70:
        grade = "B"
    elif nilai >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    print("\nNama:", nama)
    print("Nilai akhir:", nilai)
    print("Grade:", grade)
    print("Status:", status)


# Input nama
nama = input("Masukkan nama: ")

while not nama.replace(" ", "").isalpha():
    print("Nama harus menggunakan huruf!")
    nama = input("Masukkan nama: ")


# Input nilai tugas
while True:
    try:
        tugas = float(input("Masukkan nilai tugas: "))
        if tugas >= 0 and tugas <= 100:
            break
        else:
            print("Nilai harus 0-100!")
    except:
        print("Masukkan angka!")


# Input nilai UTS
while True:
    try:
        uts = float(input("Masukkan nilai UTS: "))
        if uts >= 0 and uts <= 100:
            break
        else:
            print("Nilai harus 0-100!")
    except:
        print("Masukkan angka!")


# Input nilai UAS
while True:
    try:
        uas = float(input("Masukkan nilai UAS: "))
        if uas >= 0 and uas <= 100:
            break
        else:
            print("Nilai harus 0-100!")
    except:
        print("Masukkan angka!")


# Memanggil fungsi
hitung_nilai(nama, tugas, uts, uas)
