# --- 1. SIAPKAN TOPLES PENGHITUNG HURUF DAN NILAI KELAS ---
jumlah_a = 0
jumlah_b = 0
jumlah_c = 0
jumlah_d = 0
jumlah_e = 0
total_nilai = 0

# Trik Rekor Juara & Juru Kunci:
# Nilai tertinggi diisi angka sangat kecil (-1), agar nilai pertama pasti melewatinya
nilai_tertinggi = -1
nama_tertinggi = ""

# Nilai terendah diisi angka sangat besar (101), agar nilai pertama pasti lebih kecil darinya
nilai_terendah = 101
nama_terendah = ""

# --- 2. PANGGIL 10 MAHASISWA SECARA BERURUTAN (1 SAMPAI 10) ---
for i in range(1, 11):
    print("--- Mahasiswa ke-%d ---" % i)
    nama = input("Nama        : ")

    # Minta nilai Tugas (paksa isi antara 0 sampai 100)
    while True:
        nilai_tugas = int(input("Nilai tugas : "))
        if 0 <= nilai_tugas <= 100:
            break
        print("Nilai harus 0-100!")

    # Minta nilai UTS (paksa isi antara 0 sampai 100)
    while True:
        nilai_uts = int(input("Nilai UTS   : "))
        if 0 <= nilai_uts <= 100:
            break
        print("Nilai harus 0-100!")

    # Minta nilai UAS (paksa isi antara 0 sampai 100)
    while True:
        nilai_uas = int(input("Nilai UAS   : "))
        if 0 <= nilai_uas <= 100:
            break
        print("Nilai harus 0-100!")

    # --- 3. HITUNG NILAI AKHIR (TUGAS 30%, UTS 30%, UAS 40%) ---
    nilai_akhir = (nilai_tugas * 30 + nilai_uts * 30 + nilai_uas * 40) / 100

    # --- 4. TENTUKAN HURUF KATEGORI & MASUKKAN KE TOPLESNYA ---
    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_a += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_b += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_c += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_d += 1
    else:
        kategori = "E"
        jumlah_e += 1

    # Cetak hasil rapor mahasiswa saat ini
    print(">>", nama)
    print("   Tugas %d | UTS %d | UAS %d" % (nilai_tugas, nilai_uts, nilai_uas))
    print("   Nilai akhir %.2f | Kategori %s" % (nilai_akhir, kategori))

    # Tambahkan nilai mahasiswa ini ke total kelas
    total_nilai += nilai_akhir

    # Cek apakah memecahkan rekor nilai tertinggi atau terendah
    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama
    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

# --- 5. CETAK REKAPITULASI KELAS ---
print("=== REKAP KELAS ===")
print("Jumlah A:", jumlah_a)
print("Jumlah B:", jumlah_b)
print("Jumlah C:", jumlah_c)
print("Jumlah D:", jumlah_d)
print("Jumlah E:", jumlah_e)
print("Tertinggi : %.2f (%s)" % (nilai_tertinggi, nama_tertinggi))
print("Terendah  : %.2f (%s)" % (nilai_terendah, nama_terendah))
print("Rata-rata : %.2f" % (total_nilai / 10))
