print("\n===== GAJI MINGGUAN KARYAWAN =====")
total_gaji = 0

for hari in range (1, 8):
    print("\nKaryawan Hari Ke -", hari)

    jam_lembur = int(input("Masukkan Jam Kerja Lembur :"))
    while jam_lembur < 0 or jam_lembur > 8:
        print("Jam Lembur tidak sesuai")
        jam_lembur = int(input("Masukkan Ulang jam lembur :"))

    if jam_lembur == 0:
        upah = 0
    elif jam_lembur >= 1 and jam_lembur <= 3:
        upah = jam_lembur * 25000
    elif jam_lembur == 4:
        upah = 100000
    elif jam_lembur == 6:
        upah = 200000
    elif jam_lembur == 8:
        upah = 300000
    else:
        upah = 0

    shift = input("Apakah anda bekerja shift malam? (ya/tidak) :")
    if shift == "ya":
        upah_shift = 50000
    else :
        upah_shift = 0

    gaji_pokok = 100000
    gaji_hari = gaji_pokok + upah + upah_shift

    print("Gaji Pokok     : Rp.", gaji_pokok)
    print("Upah Lembur    : Rp.", upah)
    print("Tambahan Shift : Rp.", upah_shift)
    print("Gaji Harian    : Rp.", gaji_hari)
    if jam_lembur == 5 or jam_lembur == 7 :
        print("Jam lembur tidak memiliki ketentuan upah")

    total_gaji += gaji_hari

print("\n===== REKAPITULASI AKHIR ======")
print("Total Gaji selama 7 Hari : Rp.", total_gaji) 
