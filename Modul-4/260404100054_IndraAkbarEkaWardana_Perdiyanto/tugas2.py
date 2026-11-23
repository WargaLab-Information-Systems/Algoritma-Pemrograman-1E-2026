# total_gaji = 0

# for hari in range(1, 8):
#     print("Hari ke-", hari)

#     lembur = int(input("Jam lembur: "))

#     while lembur < 0 or lembur in [5, 7]:
#         print("Jam lembur tidak valid!")
#         lembur = int(input("Masukkan ulang jam lembur: "))

#     if lembur > 8:
#         print("Jam lembur melebihi batas!")
#         upah = 0
#     elif lembur <= 3:
#         upah = lembur * 25000
#     elif lembur == 4:
#         upah = 100000
#     elif lembur == 6:
#         upah = 200000
#     else:
#         upah = 300000

#     shift = input("Shift malam? (ya/tidak): ")

#     gaji = 100000 + upah

#     if shift == "ya":
#         gaji = gaji + 50000

#     total_gaji = total_gaji + gaji

#     print("Gaji hari ini: Rp", gaji)
#     print()

# print("Total gaji seminggu: Rp", total_gaji)


total_gaji = 0

for hari in range(1, 8):
    print("Hari ke-", hari)

    lembur = int(input("Jam lembur: "))

    while lembur < 0:
        print("Jam lembur tidak valid!")
        lembur = int(input("Masukkan ulang jam lembur: "))

    while lembur == 5:
        print("Jam lembur tidak valid!")
        lembur = int(input("Masukkan ulang jam lembur: "))

    while lembur == 7:
        print("Jam lembur tidak valid!")
        lembur = int(input("Masukkan ulang jam lembur: "))

    if lembur > 8:
        print("Jam lembur melebihi batas!")
        upah = 0
    elif lembur <= 3:
        upah = lembur * 25000
    elif lembur == 4:
        upah = 100000
    elif lembur == 6:
        upah = 200000
    else:
        upah = 300000

    shift = input("Shift malam? (ya/tidak): ")

    gaji = 100000 + upah

    if shift == "ya":
        gaji = gaji + 50000

    total_gaji = total_gaji + gaji

    print("Gaji hari ini: Rp", gaji)
    print()

print("Total gaji seminggu: Rp", total_gaji)
