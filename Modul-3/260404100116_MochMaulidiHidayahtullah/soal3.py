total = 0
a = 0
b = 0
c = 0
d = 0
e = 0

tertinggi = 0
terendah = 100

for i in range(1, 11):
    print("Mahasiswa ke-", i)

    nama = input("Nama mahasiswa: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    akhir = tugas * 30 / 100 + uts * 30 / 100 + uas * 40 / 100

    if akhir >= 85:
        nilai = "A"
        a = a + 1
    elif akhir >= 75:
        nilai = "B"
        b = b + 1
    elif akhir >= 65:
        nilai = "C"
        c = c + 1
    elif akhir >= 50:
        nilai = "D"
        d = d + 1
    else:
        nilai = "E"
        e = e + 1

    print("Nama:", nama)
    print("Nilai akhir:", akhir)
    print("Kategori:", nilai)

    total = total + akhir

    if i == 1:
        tertinggi = akhir
        terendah = akhir
        nama1 = nama
        nama2 = nama
    else:
        if akhir > tertinggi:
            tertinggi = akhir
            nama1 = nama

        if akhir < terendah:
            terendah = akhir
            nama2 = nama

print("Jumlah nilai A:", a)
print("Jumlah nilai B:", b)
print("Jumlah nilai C:", c)
print("Jumlah nilai D:", d)
print("Jumlah nilai E:", e)

print("Nilai tertinggi:", tertinggi)
print("Nama mahasiswa:", nama1)

print("Nilai terendah:", terendah)
print("Nama mahasiswa:", nama2)

print("Rata-rata kelas:", total / 10)
