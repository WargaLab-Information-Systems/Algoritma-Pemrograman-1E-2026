asisten = []

while True:
    nama = input("Masukkan nama asisten: ")

    if nama == "cukup":
        break

    asisten.append(nama)
asisten_awal = tuple(asisten)
tambahan = input("\nMasukkan nama asisten tambahan: ")
asisten_akhir = asisten_awal + (tambahan,)
hari = []

while True:
    nama_hari = input("Masukkan hari tugas: ")

    if nama_hari == "cukup":
        break

    hari.append(nama_hari)
hari_akhir = tuple(hari)
print("\n=== DATA PENGECUALIAN ===")
nama_izin = input("Nama asisten yang dikecualikan: ")
hari_izin = input("Hari yang dikecualikan: ")
print("\n=== JADWAL SHIFT ASISTEN ===")

for nama in asisten_akhir:
    for nama_hari in hari_akhir:
        if nama == nama_izin and nama_hari == hari_izin:
            continue

        print(nama, "-", nama_hari)