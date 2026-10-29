n = int(input("Masukkan n: "))
for baris_kiri in range(1, n + 1):
    baris_kanan = n - baris_kiri + 1
    # piramida kiri (melebar ke bawah)
    for spasi in range(n - baris_kiri):
        print("  ", end="")
    for angka_naik in range(1, baris_kiri + 1):
        print(angka_naik, end=" ")
    for angka_turun in range(baris_kiri - 1, 0, -1):
        print(angka_turun, end=" ")
    for spasi in range(n - baris_kiri):   
        print("  ", end="")
    print("   ", end="")  
    # piramida kanan (mengecil ke bawah)
    for spasi in range(n - baris_kanan):
        print("  ", end="")
    for angka_naik in range(1, baris_kanan + 1):
        print(angka_naik, end=" ")
    for angka_turun in range(baris_kanan - 1, 0, -1):
        print(angka_turun, end=" ")
    print()