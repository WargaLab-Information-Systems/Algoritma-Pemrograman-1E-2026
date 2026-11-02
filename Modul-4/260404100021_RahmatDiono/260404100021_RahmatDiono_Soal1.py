baris = int(input('masukkan baris lampu: '))
lamp = int(input('masukkan jumlah lampu per baris: '))

for i in range(1, baris+1):
    print(f'baris ke-{i}') # Outer loop
 
    for j in range(1, lamp+1):   # Inner loop
        if j % 3 == 0:
            print(' ', 'gangguan', end=' ') # lampu mengalami gangguan pada kelipatan 3
        else:
            print(f'lampu{j}', end=' ') # lampu ke-n
    print()
print('Periksa sumber listrik utama taman.')