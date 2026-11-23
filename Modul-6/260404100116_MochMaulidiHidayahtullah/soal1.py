anggota = []

while True:
    nama = input("Masukkan nama anggota: ").strip()

    if nama.lower() == "selesai":
        break

    if not nama.isalpha():
        print("Nama harus berupa huruf!")
        continue

    if len(nama) < 4 or len(nama) > 20:
        print("Nama harus 4-20 karakter!")
        continue

    anggota.append(nama)

print("\nHasil Pemeriksaan:")

for nama in anggota:
    if nama.lower() == "admin" or len(nama) <= 4:
        print(nama, "- Nama Tidak Valid")

    else:
        print(nama, "- Nama Valid")

while True:
    hapus = input("\nMasukkan nama penyusup: ")

    if hapus in anggota:
        anggota.remove(hapus)
        print("Nama berhasil dihapus!")
        break
    else:
        print("Nama tidak ditemukan, masukkan lagi!")

print("\nDaftar Anggota Akhir:", anggota)
