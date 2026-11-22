# --- 1. MINTA INPUT TINGGI (HARUS 2 SAMPAI 15) ---
while True:
    tinggi = int(input("Tinggi setengah menara (2-15): "))
    # Jika angka pas di antara 2 dan 15, boleh lanjut (keluar dari loop)
    if 2 <= tinggi <= 15:
        break
    print("Di luar rentang, ulangi!")

# --- 2. BAGIAN ATAS MENARA: DARI BARIS 1 NAIK KE PUNCAK ---
for baris in range(1, tinggi + 1):
    isi_baris = ""
    # Angka NAIK: dari 1 sampai nomor baris (misal baris 3: 1, 2, 3)
    for angka in range(1, baris + 1):
        # Trik % 10: kalau angka 10 jadi 0, 11 jadi 1 (biar tetap ramping 1 karakter)
        isi_baris = isi_baris + str(angka % 10)
    # Angka TURUN: setelah puncak mundur ke 1 (misal setelah 3: 2, 1)
    for angka in range(baris - 1, 0, -1):
        isi_baris = isi_baris + str(angka % 10)
    # Cetak spasi di depan agar terdorong ke tengah membentuk piramida
    print(" " * (tinggi - baris) + isi_baris)

# --- 3. BAGIAN BAWAH MENARA: DARI BAWAH PUNCAK MUNDUR KE BARIS 1 ---
for baris in range(tinggi - 1, 0, -1):
    isi_baris = ""
    # Angka NAIK
    for angka in range(1, baris + 1):
        isi_baris = isi_baris + str(angka % 10)
    # Angka TURUN
    for angka in range(baris - 1, 0, -1):
        isi_baris = isi_baris + str(angka % 10)
    # Cetak spasi di depan agar tetap simetris
    print(" " * (tinggi - baris) + isi_baris)
