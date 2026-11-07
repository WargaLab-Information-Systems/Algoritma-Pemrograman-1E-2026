total_gaji = 0
print("=== Program Penghitung Gaji Minggu Karyawan ===")
for i in range(1, 8):
    print(f"\n Hari ke {i}")
    gaji_harian = 100000
    
    shift_malam = input("Apakah bekerja shift malam? (y/t): ")
    tambah_shift = 50000 if shift_malam == 'y' else 0
    jam_lembur = int(input("masukkan jam lembur (0-8 jam): "))

    while jam_lembur > 8:
        print("lembur melebihi batas 8 jam! masukkan ulang.")
        jam_lembur = int(input("masukkan jam lembur (0-8 jam): "))

    if 1 <= jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 5:
        upah_lembur = 125000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 7:
        upah_lembur = 225000
    elif jam_lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    gaji_hari_ini = gaji_harian + tambah_shift + upah_lembur
    total_gaji += gaji_hari_ini
    print(f"gaji hari ke-{i}: Rp {gaji_hari_ini:,}")

print("\n" + "="*40)
print(f"total gaji mingguan selama 7 hari: Rp {total_gaji:,}")
print("="*40)