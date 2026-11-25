asisten_awal = []

while True:
    nama = input("Masukkan nama asisten awal (cukup untuk berhenti): ")

    if nama.lower() == "cukup":
        break

    asisten_awal.append(nama)
asisten_terkunci = tuple(asisten_awal)

tambahan = input("\nMasukkan nama asisten tambahan: ")

asisten_akhir = list(asisten_terkunci) + [tambahan]
hari = []

while True:
    nama_hari = input("Masukkan hari tugas (cukup untuk berhenti): ")

    if nama_hari.lower() == "cukup":
        break

    hari.append(nama_hari)
                
hari_terkunci = tuple(hari)

pengecualian_asisten = input("\nMasukkan nama asisten yang dikecualikan: ")
pengecualian_hari = input("Masukkan hari yang dikecualikan: ")

print("\n=== JADWAL SHIFT ASISTEN LABORATORIUM ===")

for nama_asisten in asisten_akhir:
    for nama_hari in hari_terkunci:

        if nama_asisten == pengecualian_asisten and nama_hari == pengecualian_hari:
            continue

        print(nama_asisten, "-", nama_hari)
