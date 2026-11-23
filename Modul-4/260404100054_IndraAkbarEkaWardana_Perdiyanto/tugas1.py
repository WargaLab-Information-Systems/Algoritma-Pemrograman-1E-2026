baris = int(input("Masukkan jumlah baris lampu: "))
jumlah = int(input("Masukkan jumlah lampu setiap baris: "))

for i in range(1, baris + 1):
    print("Baris", i)

    for j in range(1, jumlah + 1):
        if j % 3 == 0:
            print("Lampu", j, "mengalami gangguan")
        elif j % 2 == 0:
            print("Lampu", j, "mengalami kerusakan")
        else:
            print("Lampu", j, "berfungsi normal")
        

print("Periksa sumber listrik utama taman!")
