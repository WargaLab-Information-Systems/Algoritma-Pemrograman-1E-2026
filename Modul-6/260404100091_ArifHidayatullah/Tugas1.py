Daftar_anggota = []
print("=== Program pendaftaran klub robotika ===")
print("ketik 'selesai' jika sudah selesai memasukkan nama.\n")
while True:
    nama = input("Masukkan nama calon anggota: ")
    if nama.lower() == "selesai":
        break
    Daftar_anggota.append(nama)
print("\n--- Hasil Evaluasi pendaftaran ---")
for nama in Daftar_anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(f"Nama '{nama}' : Tidak Valid (Nama 'admin' atau panjang kurang dari 4 karakter)")
    else:
        print(f"Nama '{nama}' : Valid")
print("\n--- penghapusan penyusup ---")
penyusup = input("masukkan nama spesifik yang dicurigai sebagai penyusup: ")
if penyusup in Daftar_anggota:
    Daftar_anggota.remove(penyusup)
    print(f"Berhasil! Nama '{penyusup}' telah dihapus oleh sistem")
    print("daftar anggota setelah pembersihan:", Daftar_anggota)
else:
    print(f"Nama '{penyusup}' tidak ditemukan didalam daftar pendaftaran.")
    print("program tetap berjalan dengan aman tanpa eror/crash.")