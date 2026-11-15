def penjadwalan_shift():
    #Menginput nama-nama asistensi awal secara berulang hingga 'cukup'
    print("=== Masukkan Nama Assistensi Awal ===")
    asisten_awal = []
    while True:
        Nama = input("Masukkan nama asistensi (ketik 'cukup' untuk selesai): ").strip()
        if Nama.lower() == "cukup":
            break
        if Nama:
            asisten_awal.append(Nama)
    #Mengunci secara permanen menggunakan tuple
    asisten_awal = tuple(asisten_awal)
    print(f"Data asistensi awal dikunci: {asisten_awal}\n")
    #Meminta satu nama asisten tambahan yang mendadak bergabung
    print("=== Masukkan Asisten Tambahan ===")
    asisten_tambahan = input("Masukkan nama 1 asisten tambahan: ").strip()
    # Menggabungkan dengan data asisten awal ke dalam wadah yang baru (tuple/list baru)
    wadah_baru = list(asisten_awal)
    if asisten_tambahan and asisten_tambahan not in wadah_baru:
        wadah_baru.append(asisten_tambahan)
    wadah_baru = tuple(wadah_baru)
    print(f"Wadah asisten baru setelah digabung: {wadah_baru}\n")
    #Meminta input nama-nama hari tugas hingga mengetik "cukup"
    print("=== Masukkan Hari Tugas ===")
    hari_tugas = []
    while True:
        hari = input("Masukkan nama hari (ketik 'cukup' untuk selesai): ").strip()
        if hari.lower() == "cukup":
            break
        if hari:
            hari_tugas.append(hari)            
    # Mengunci hari tugas (menggunakan tuple)
    hari_tugas = tuple(hari_tugas)
    print(f"Data hari tugas dikunci: {hari_tugas}\n")
    #Memasangkan setiap asisten akhir dengan setiap hari yang tersedia
    print("=== Pengecualian Shift ===")
    asisten_pengecualian = input("Masukkan nama asisten untuk pengecualian: ").strip()
    hari_pengecualian = input("Masukkan hari untuk pengecualian (misal: karena ada kuliah): ").strip()
    print("\n" + "="*30)
    print("HASIL KOMBINASI SHIFT JADWAL")
    print("="*30)

    jumlah_berhasil = 0
    #Memasangkan setiap asisten di wadah_baru dengan setiap hari di hari_tugas
    for asisten in wadah_baru:
        for hari in hari_tugas:
            #Memeriksa apakah kombinasi ini merupakan pengecualian
            if asisten.lower() == asisten_pengecualian.lower() and hari.lower() == hari_pengecualian.lower():
                continue
            
            #Tampilkan kombinasi shift yang berhasil dibuat
            print(f"Asisten: {asisten} | Hari: {hari}")
            jumlah_berhasil += 1     
    print("="*30)
    print(f"Total kombinasi shift yang berhasil dibuat: {jumlah_berhasil}")
#Menjalankan fungsi program
penjadwalan_shift()