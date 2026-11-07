print("\n===== PEMERIKSAAN LAMPU TAMAN KOTA =====")

b = int(input("Masukkan Jumlah Baris Lampu :"))
j = int(input("Masukkan Jumlah Lampu :"))

for c in range (1, b+1):
    print("Baris Lampu Ke -", c)

    for a in range (1, j+1):
        if a % 3 == 0:
            print("Lampu ke -", a, "Lampu mengalami gangguan")
        else :
            print("Lampu Ke -", a, "Lampu berfungsi normal")
    print()

print("Periksa Kembali Sumber Listrik Utama")