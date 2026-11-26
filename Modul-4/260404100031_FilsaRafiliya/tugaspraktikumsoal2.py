total_gaji = 0

for harikerja in range(1,8):
    print(f"\nHari kerja ke-{harikerja}")
    gaji_hari = 100000
    print ("gaji pokok harian: ", gaji_hari)

    while True:
        lembur = int(input("masukkan jam lembur: "))
        if lembur >8:
            print ("jam lembur melebihi batas, tidak dapat menghitung upah")
        else:
            break
    while True:
        shift = input("shift malam? (y/t): ")
        if shift == "y" or shift == "t":
            break
        print ("input tidak valid, ketik y atau t.")

    if lembur <=3:
        perjam = 25000
        upah_lembur = lembur * perjam
        print ("mendapat upah lembur sebesar", upah_lembur)
    elif lembur == 4:
        upah_lembur = 100000
        print ("mendapat upah lembur sebesar", upah_lembur)
    elif lembur == 6:
        upah_lembur = 200000
        print ("mendapat upah lembur sebesar", upah_lembur)
    elif lembur == 8:
        upah_lembur = 300000
        print ("mendapat upah lembur sebesar", upah_lembur)
    
    tambahan = 50000 if shift == "y" else 0
    if shift == "y":
        print ("mendapat upah tambahan sebesar", tambahan)

    gaji_hari += upah_lembur + tambahan
    total_gaji += gaji_hari

    print (f"gaji hari ke {harikerja}: Rp{gaji_hari}")

print (f"\nTotal gaji mingguan: Rp{total_gaji}")