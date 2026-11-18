asisten = []

while True:
    nama = input('Masukkan nama asisten (type "cukup" untuk selesai): ')
    if nama.lower() == 'cukup':
        break
    asisten.append(nama)

asisten_awal = tuple(asisten)
tambahan = input('Masukkan nama asisten tambahan: ')
asisten_akhir = asisten_awal + (tambahan,)
hari = []

while True:
    nama_hari = input('Masukkan hari tugas (type "cukup" untuk selesai): ')
    if nama_hari.lower() == 'cukup':
        break
    hari.append(nama_hari)

hari_tugas = tuple(hari)
pengecualian_asisten = input('Masukkan nama asisten yang dikecualikan: ')
pengecualian_hari = input('Masukkan hari yang dikecualikan: ')

print('jadwal asistensi')
for nama in asisten_akhir:
    for nama_hari in hari_tugas:
        if nama == pengecualian_asisten and nama_hari == pengecualian_hari:
            continue
        print(nama, '-', nama_hari)