anggota = []

while True:
    nama = input("Masukkan nama (selesai untuk berhenti): ")

    if nama.lower() == "selesai":
        break

    anggota.append(nama)

print("=== HASIL EVALUASI ===")

for nama in anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, ": Nama tidak valid")
    else:
        print(nama, ": Nama valid")

penyusup = input("\nMasukkan nama penyusup: ")

if penyusup in anggota:
    anggota.remove(penyusup)
    print("Nama berhasil dihapus.")
else:
    print("Nama tidak ditemukan.")

print("\n=== DAFTAR ANGGOTA AKHIR ===")
print(anggota)
