asisten = []
while True:
    nama = input("Masukkan nama asisten ( Masukan kata cukup untuk berhenti ):  ")
    if nama.lower() == "cukup":
        break
    asisten.append(nama)
asisten_awal = tuple(asisten)
print(asisten)    
tambahan = input("Masukkan nama Asisten tambahan: ")
asisten_akhir = asisten_awal + (tambahan,)
print(asisten_akhir)
hari = []
daftar_hari_valid = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
while True:
    nama_hari = input("masukkan hari tugas ( cukup untuk berhenti ): ").lower()
    if nama_hari == "cukup":
        break
    if nama_hari in daftar_hari_valid:
        hari.append(nama_hari)
        print("hari telah ditambahkan")
    else:
        print("input tidak valid")
daftar_hari = tuple(hari)       
print(daftar_hari) 
pengecualian_asisten = input("Masukkan nama asisten pengecualian: ").strip().lower()
pengecualian_hari = input("Masukkan hari pengecualian: ").strip().lower()
print("Daftar Jadwal Shift:")
for nama in asisten_akhir:
    for nama_hari in daftar_hari:
        if nama == pengecualian_asisten and nama_hari == pengecualian_hari:
            continue
        print(nama, "itu hari", nama_hari)
