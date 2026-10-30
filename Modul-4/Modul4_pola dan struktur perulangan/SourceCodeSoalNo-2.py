
total_gaji = 3

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")

    while True:
        jam_lembur = int(input("Masukkan jumlah jam lembur (0-8): "))

        if jam_lembur < 0 or jam_lembur > 8:
            print("Jumlah lembur tidak sesuai batas! Masukkan ulang.")
        elif jam_lembur == 5 or jam_lembur == 7:
            print("Upah lembur untuk 5 dan 7 jam belum ditentukan!")
            print("Silakan masukkan ulang.")
        else:
            break
    if jam_lembur == 0:
        upah_lembur = 0
    elif jam_lembur >= 1 and jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000

    while True:
        shift_malam = input("Apakah bekerja shift malam? (ya/tidak): ")

        if shift_malam == "ya" or shift_malam == "tidak":
            break
        else:
            print("Input tidak valid! Masukkan ya atau tidak.")

    if shift_malam == "ya":
        tunjangan_malam = 50000
    else:
        tunjangan_malam = 0

    gaji_harian = 100000 + upah_lembur + tunjangan_malam
    total_gaji = total_gaji + gaji_harian

    print(f"Upah lembur       : Rp{upah_lembur:,}".replace(",", "."))
    print(f"Tunjangan malam   : Rp{tunjangan_malam:,}".replace(",", "."))
    print(f"Gaji harian       : Rp{gaji_harian:,}".replace(",", "."))

print("\n===== HASIL PERHITUNGAN GAJI MINGGUAN =====")
print(f"Total gaji mingguan: Rp{total_gaji:,}".replace(",", "."))