daftar_nama = []
while True:
    nama = input("Masukan nama anggota(Jika sudah inputkan kata selesai): ")
    if nama.lower() == "selesai":
        break
    daftar_nama.append(nama)
print("hasil Pemeriksaan nama: ")   
for nama in daftar_nama:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")
penyusup = input("Masukan nama penyusup yang ingin di hapus:  ")
if penyusup in daftar_nama:
    daftar_nama.remove(penyusup)
    print("Nama berhasil dihapus")
else:
    print("Nama tidak ditemukan")
print("daftar anggota akhir:", daftar_nama)               