daftar = []
daftarHari = []

namaAsisten = input("masukkan nama: ")
while namaAsisten != "cukup":
    daftar.append(namaAsisten)
    namaAsisten = input("masukkan nama: ")
asisten = tuple(daftar)

print("---- satu tambahan orang----")
tambahan = input("masukkan nama: ")
asistenAkhir = asisten + (tambahan, )

hari = input("masukkan hari: ")
while hari != "cukup":
    daftarHari.append(hari)
    hari = input("masukkan hari: ")
Hari = tuple(daftarHari)

AsistenA = input("masukkan nama asisten pengecualian: ")
HariA = input ("masukkan hari pengecualian: ")

jadwal =[]
for a in asistenAkhir:
    for h in Hari: 
        if a == AsistenA and h == HariA:
            continue
        jadwal.append ((a, h))

print ("\nJadwal Shift: ")
for a, h in jadwal:
    print (f"{a} - {h}")