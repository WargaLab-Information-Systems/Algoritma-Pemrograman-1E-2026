def input_nama(asisten):
    while True:
        teks = input(asisten)
        if teks != "" and teks.isalpha():
            return teks
        print("Input tidak valid! Harus berupa nama (huruf saja)")

list_awal = []
while True:
    nama = input_nama("Masukkan nama asisten awal (ketik 'cukup' untuk berhenti): ")
    if nama == "cukup":
        break
    list_awal.append(nama)
asisten_awal = tuple(list_awal)
tambahan = input_nama("Masukkan nama asisten tambahan yang baru bergabung: ")
asisten_akhir = asisten_awal + (tambahan,)

list_hari = []
while True:
    hari = input_nama("Masukkan nama hari  (ketik 'cukup' untuk berhenti): ")
    if hari == "cukup":
        break
    list_hari.append(hari)
hari_tugas = tuple(list_hari)

asisten_x = input_nama("Masukkan nama asisten yang dikecualikan: ")
hari_x = input_nama("Masukkan hari pengecualiannya: ")

print("\n=== Jadwal Shift ===")
jumlah = 0
for asisten in asisten_akhir:
    for hari in hari_tugas:
        if asisten == asisten_x and hari == hari_x:
            continue
        jumlah += 1
        print(str(jumlah) + ". " + asisten + " - " + hari)

if jumlah == 0:
    print("Tidak ada shift yang berhasil dibuat.")