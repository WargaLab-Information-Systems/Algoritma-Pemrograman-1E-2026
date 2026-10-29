jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu setiap baris: "))
baris = 0
for baris in range(1, jumlah_baris + 1):
    print("Baris", baris)
    baris = baris + 1
    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print("Lampu", lampu, ": Mengalami gangguan")
        else:
            print("Lampu", lampu, ": Berfungsi normal")

print("Periksa sumber listrik utama taman!")