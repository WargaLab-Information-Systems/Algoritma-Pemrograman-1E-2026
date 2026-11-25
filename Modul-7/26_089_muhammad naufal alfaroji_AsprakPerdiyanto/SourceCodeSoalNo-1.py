tugas = {}  

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas selesai & belum")
    print("0. Keluar")

    try:
        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            nama = input("Nama tugas: ").strip()
            if nama == "":
                raise ValueError("Nama tugas tidak boleh kosong.")
            if nama in tugas:
                raise ValueError("Tugas sudah ada.")
            tugas[nama] = "Belum selesai"
            print(f"Tugas '{nama}' ditambahkan.")

        elif pilih == "2":
            if not tugas:
                print("Belum ada tugas.")
            for nama, status in tugas.items():
                print(f"- {nama} [{status}]")

        elif pilih == "3":
            nama = input("Nama tugas yang selesai: ").strip()
            tugas[nama]  
            tugas[nama] = "Selesai"
            print(f"Tugas '{nama}' ditandai selesai.")

        elif pilih == "4":
            nama = input("Nama tugas yang dihapus: ").strip()
            del tugas[nama]  
            print(f"Tugas '{nama}' dihapus.")

        elif pilih == "5":
            selesai = list(tugas.values()).count("Selesai")
            print(f"Selesai: {selesai}")
            print(f"Belum selesai: {len(tugas) - selesai}")

        elif pilih == "0":
            print("Terima kasih!")
            break

        else:
            print("Menu tidak valid.")

    except KeyError:
        print("Error: tugas yang dituju tidak ditemukan.")