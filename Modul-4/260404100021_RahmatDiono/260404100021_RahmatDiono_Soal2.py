gaji = 0

for i in range(1, 8):
    print(f'Hari ke-{i}')
    lembur = int(input('Masukkan jam lembur: '))
    while lembur not in [0, 1, 2, 3, 4, 6, 8]:
        print('Jam lembur tidak valid, masukkan ulang!')
        lembur = int(input('Masukkan jam lembur: '))

    while True:
        shift = input('Kerja shift malam? (y/n): ').lower()
        if shift != 'y' and shift != 'n':
            continue
        else:
            break
    harian = 100000

    if lembur <= 3:
        harian += lembur * 25000
    elif lembur == 4:
        harian += 100000
    elif lembur == 6:
        harian += 200000
    elif lembur == 8:
        harian += 300000
    if shift == 'y':
        harian += 50000
    gaji += harian
    print(f'Gaji hari ini: Rp{harian}')
print(f'Total gaji mingguan: Rp{gaji}')
