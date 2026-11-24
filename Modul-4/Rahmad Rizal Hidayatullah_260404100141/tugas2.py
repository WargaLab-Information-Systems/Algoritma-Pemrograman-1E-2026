total_gaji = 0

for hari in range(1, 8):
    print("\nHari ke-", hari)

# lembur
    while True:
        lembur = int(input("Masukkan jam lembur: "))

        if lembur > 8:
            print("Jam lembur melebihi batas 8 jam. Masukkan ulang.")
        elif lembur in [0, 1, 2, 3, 4, 6, 8]:
            break
        else:
            print("Jam lembur tidak sesuai ketentuan. Masukkan ulang.")


    gaji = 100000

    if lembur >= 1 and lembur <= 3:
        gaji = gaji + (lembur * 25000)
    elif lembur == 4:
        gaji = gaji + 100000
    elif lembur == 6:
        gaji = gaji + 200000
    elif lembur == 8:
        gaji = gaji + 300000

    shift = input("Apakah shift malam? (ya/tidak): ").lower()

    while shift != "ya" and shift != "tidak":
        print("Jawaban harus ya atau tidak!")
        shift = input("Apakah shift malam? (ya/tidak): ").lower()

    if shift == "ya":
        gaji = gaji + 50000

    #
    print("Gaji hari ke-", hari, ": Rp", gaji)
    total_gaji = total_gaji + gaji
    print("Total gaji sementara: Rp", total_gaji)

# Total setelah 7 hari
print("\n==============================")
print("Total gaji selama 7 hari: Rp", total_gaji)
print("==============================")
