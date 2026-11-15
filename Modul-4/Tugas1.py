jumlah_baris = int(input("masukkan jumlah baris lampu: "))
jumlah_lampu_per_baris = int(input("masukkan jumlah lampu pada setiap baris: "))
for i in range(1, jumlah_baris + 1):
    print(f"\nMemeriksa baris ke -{i}")
    for j in range(1, jumlah_lampu_per_baris + 1):
        if j % 3 == 0:
            print(f"lampu ke {j}: mengalami gangguan")
        else:
            print(f"lampu ke {j}: berfungsi normal")

print("\nSemua lampu telah diperiksa. Silakan periksa sumber listrik utama taman")
