baris = int(input("masukkan jumlah baris lampu: "))
jmlhlampu = int(input("masukkan jumlah lampu pada setiap baris: "))

for b in range(1, baris + 1):
    print(f"Pemeriksaan baris ke-{b}")
    for l in range(1, jmlhlampu + 1):
        if l % 3 == 0:
            print (' ', f"lampu nomor {l} : mengalami gangguan")
        else:
            print (' ', f"lampu nomor {l} : berfungsi normal")

print ("\nSeluruh lampu telah diperiksa. silahkan periksa sumber listrik utama taman.")