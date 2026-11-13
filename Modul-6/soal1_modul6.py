daftar = []

nama = input("Masukkan nama calon anggota: ")
while nama != "selesai":
    daftar.append(nama)
    nama = input("Masukkan nama calon anggota: ")

print("\n--- Hasil Evaluasi---")
for nama in daftar:
    if nama == "admin" or len(nama) < 4:
        print(nama, ": TIDAK VALID")
    else:
        print(nama, ": VALID")

while True:
    penyusup = input("Ketik nama yang dicurigai sebagai penyusup: ")

    if penyusup not in daftar:
        print(penyusup, "tidak ditemukan di pendaftaran.")
        continue

    daftar.remove(penyusup)
    print(penyusup, "berhasil dihapus.")
    break

daftar_akhir = tuple(daftar)
print("\nDaftar akhir anggota:", daftar_akhir)