mahasiswa = 0
nilaiA = 0
nilaiB = 0
nilaiC = 0
nilaiD = 0
nilaiE = 0
nilaitertinggi = 0
namant = ""
nilaiterendah = 100
namant2 = ""
totalnilai = 0

while mahasiswa != 10:
    nama = input("masukkan nama: ")
    nilaiTugas = int(input("masukkan nilai tugas: "))
    nilaiUTS = int(input("masukkan nilai UTS: "))
    nilaiUAS = int(input("masukkan nilai UAS: "))
    nilaiAkhir = ((nilaiTugas * 0.3)+(nilaiUTS * 0.3)+(nilaiUAS * 0.4))
    print ("nilai akhirnya adalah", nilaiAkhir)
    if nilaiAkhir >=85:
        nilaiA += 1
        print ("mendapat nilai A")
    elif nilaiAkhir >=75 and nilaiAkhir <85:
        nilaiB += 1
        print ("mendapat nilai B")
    elif nilaiAkhir >=65 and nilaiAkhir <75:
        nilaiC += 1
        print ("mendapatkan nilai C")
    elif nilaiAkhir >=50 and nilaiAkhir <65:
        nilaiD += 1
        print ("mendapat nilai D")
    else:
        nilaiE += 1
        print ("mendapat nilai E")

    totalnilai += nilaiAkhir

    if nilaiAkhir > nilaitertinggi:
        nilaitertinggi = nilaiAkhir
        namant = nama

    if nilaiAkhir < nilaiterendah:
        nilaiterendah = nilaiAkhir
        namant2 = nama

    mahasiswa += 1
#setelah semua data diproses
print ("jumlah mahasiswa yang mendapat nilai A adalah ", nilaiA, "anak")
print ("jumlah mahasiswa yang mendapat nilai B adalah ", nilaiB, "anak")
print ("jumlah mahasiswa yang mendapat nilai C adalah ", nilaiC, "anak")
print ("jumlah mahasiswa yang mendapat nilai D adalah ", nilaiD, "anak")
print ("jumlah mahasiswa yang mendapat nilai E adalah ", nilaiE, "anak")
print ("mahasiswa yang mempunyai nilai akhir paling tinggi adalah ", namant, "dengan nilai ", nilaitertinggi)
print ("mahasiswa yang mempunyai nilai akhir paling rendah adalah ", namant2, "dengan nilai ", nilaiterendah)
rata2nilai = (totalnilai / 10)
print ("rata-rata nilai akhir dari seluruh mahasiswa adalah ", rata2nilai)