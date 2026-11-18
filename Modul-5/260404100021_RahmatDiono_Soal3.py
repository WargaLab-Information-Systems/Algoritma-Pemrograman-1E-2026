def nilai(nama, tugas, uts, uas):
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    if nilai_akhir >= 85:
        grade = 'A'
    elif nilai_akhir >= 70:
        grade = 'B'
    elif nilai_akhir >= 55:
        grade = 'C'
    else : 
        grade == 'D'
    if grade == 'D':
        keterangan = 'Tidak Lulus'
    else:
        keterangan = 'Lulus'
        
    print(f'Nama: {nama}')
    print(f'Nilai Tugas: {tugas}')
    print(f'Nilai UTS: {uts}')
    print(f'Nilai UAS: {uas}')
    print(f'Nilai Akhir: {nilai_akhir}')
    print(f'grade: {grade}')
    print(f'Keterangan: {keterangan}')

nama = str(input('masukan nama: '))
tugas = int(input('masukan nilai tugas: '))
uts = int(input('masukan nilai uts: '))
uas = int(input('masukan nilai uas: '))

nilai(nama, tugas, uts, uas)