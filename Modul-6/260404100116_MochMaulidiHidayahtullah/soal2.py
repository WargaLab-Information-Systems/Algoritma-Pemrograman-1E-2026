asisten = []

print("Asisten Awal")
while True:
    nama = input("Nama asisten: ").lower()

    if nama == "cukup":
        break

    if not nama.replace(" ", "").isalpha():
        print("Nama harus berupa huruf!")
        continue

    asisten.append(nama)

asisten_awal = tuple(asisten)
print("Asisten awal:", asisten_awal)


print("\nAsisten Tambahan")
tambahan = input("Nama tambahan: ").lower()

while not tambahan.replace(" ", "").isalpha():
    print("Nama harus berupa huruf!")
    tambahan = input("Nama tambahan: ").lower()

asisten_akhir = asisten_awal + (tambahan,)
print("Asisten akhir:", asisten_akhir)


print("\nHari Tugas")
hari = []
daftar_hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

while True:
    h = input("Nama hari: ").lower()

    if h == "cukup":
        break

    if h not in daftar_hari:
        print("Hari tidak valid!")
        continue

    hari.append(h)

hari_tugas = tuple(hari)
print("Hari tugas:", hari_tugas)


print("\nPengecualian")
while True:
    pengecualian = input("Nama asisten: ").lower()

    if pengecualian in asisten_akhir:
        break

    print("Asisten tidak ditemukan!")

while True:
    libur = input("Hari pengecualian: ").lower()

    if libur in hari_tugas:
        break

    print("Hari tidak ditemukan!")


print("\nJadwal Shift")
for nama in asisten_akhir:
    for h in hari_tugas:
        if nama == pengecualian and h == libur:
            continue

        print(nama, "-", h)
