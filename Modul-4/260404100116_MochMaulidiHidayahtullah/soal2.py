total_gaji = 0

for hari in range(1, 8):
    print("\nHari ke-", hari)

    lembur = int(input("Masukkan jam lembur (0, 1, 2, 3, 4, 6, 8): "))

    while lembur not in [0, 1, 2, 3, 4, 6, 8]:
        print("Jam lembur tidak sesuai ketentuan!")
        lembur = int(input("Masukkan ulang jam lembur: "))

    if lembur > 8:
        print("Jam lembur melebihi batas!")
        upah_lembur = 0
    elif lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    malam = input("Apakah bekerja shift malam? (y/t): ")

    if malam == "y":
        tambahan = 50000
    else:
        tambahan = 0

    gaji = 100000 + upah_lembur + tambahan
    total_gaji = total_gaji + gaji

    print("Gaji hari ini: Rp", gaji)

print("\nTotal gaji mingguan: Rp", total_gaji)
