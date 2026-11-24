def input_nama(admin):
    while True:
        nama = input(admin)
        if nama != "" and nama.isalpha():
            return nama
        print("Input tidak valid! Harus berupa nama (huruf saja)")

daftar = []
while True:
    nama = input_nama("Masukkan nama calon anggota (ketik 'selesai' untuk berhenti): ")
    if nama == "selesai":
        break
    daftar.append(nama)

print("\nHasil Pemeriksaan")
for nama in daftar:
    if nama == "admin" or len(nama) < 4:
        print(nama + " : nama tidak valid")
    else:
        print(nama + " : valid")

ada_yang_janggal= input_nama("\nMasukkan nama yang dicurigai sebagai penyusup: ")
try:
    daftar.remove(ada_yang_janggal)
    print("Nama '" + ada_yang_janggal + "berhasil dihapus dari pendaftaran")
except ValueError:
    print("Nama '" + ada_yang_janggal + "tidak ada di dalam pendaftaran")

print("\nDaftar akhir:", daftar)