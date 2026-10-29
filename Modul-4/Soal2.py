total_gaji = 0

for hari in range(1, 8):
    print("Hari ke-", hari)
    jam_lembur = int(input("Masukkan jam lembur: "))
    while jam_lembur not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        print("Jam lembur tidak sesuai ketentuan!")
        jam_lembur = int(input("Masukkan ulang jam lembur: "))
    if jam_lembur > 8:
        print("Jumlah lembur melebihi batas!")
        upah_lembur = 0
    elif jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 5:
        upah_lembur = 125000    
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 7:
        upah_lembur = 225000    
    else:
        upah_lembur = 300000
    shift = input("Shift malam? (ya/tidak): ").lower()
    if shift == "ya":
        tambahan_malam = 50000
    else:
        tambahan_malam = 0
    gaji_harian = 100000 + upah_lembur + tambahan_malam
    total_gaji = total_gaji + gaji_harian
    
    print("Gaji hari ini: Rp", gaji_harian)
print("Total gaji mingguan: Rp", total_gaji)