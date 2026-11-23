anggota = []

nama = ""

while nama != "selesai":
    nama = input("Masukkan nama anggota (ketik selesai): ")

    if nama != "selesai":
        anggota.append(nama)

print("Daftar Anggota:")

for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "- Nama tidak valid")
    else:
        print(nama, "- Nama valid")

hapus = input("Masukkan nama penyusup yang ingin dihapus: ")

if hapus in anggota:
    anggota.remove(hapus)
    print("Nama berhasil dihapus!")
else:
    print("Nama tidak ditemukan!")

print("Daftar Anggota Akhir:")
print(anggota)
