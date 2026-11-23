asisten = []

nama = ""

print("Masukkan Nama Asisten Awal")

while nama != "cukup":
    nama = input("Nama Asisten (ketik cukup): ")

    if nama != "cukup":
        asisten.append(nama)

asisten_awal = tuple(asisten)

tambahan = input("Nama Asisten Tambahan: ")

asisten_akhir = asisten_awal + (tambahan,)

hari = []

nama_hari = ""

print("Masukkan Hari Tugas")

while nama_hari != "cukup":
    nama_hari = input("Nama Hari (ketik cukup): ")

    if nama_hari != "cukup":
        hari.append(nama_hari)

hari_tugas = tuple(hari)

print("Jadwal Pengecualian")

nama_khusus = input("Nama Asisten: ")
hari_khusus = input("Hari Pengecualian: ")

print("Daftar Jadwal Shift:")

for nama in asisten_akhir:
    for nama_hari in hari_tugas:

        if nama != nama_khusus or nama_hari != hari_khusus:
            print(nama, "-", nama_hari)
