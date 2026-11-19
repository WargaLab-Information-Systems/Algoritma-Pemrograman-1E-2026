tugas = {}

while True:
    print("MENU")
    print("1. Tambah tugas")
    print("2. Lihat semua tugas")
    print("3. Tandai tugas")
    print("4. Hapus tugas")
    print("5. Jumlah tugas")
    print("6. Keluar")

    pilihan = input("Masukkan pilihan (1-6): ")

    if pilihan == "1":
        nama = input("Masukkan nama tugas: ")
        if nama in tugas:
            print("Tugas sudah ada.")
        else:
            tugas[nama] = "Belum selesai"
            print("Tugas berhasil ditambahkan.")

    elif pilihan == "2":
        if len(tugas) == 0:
            print("Tidak ada tugas.")
        else:
            print("Daftar tugas:")
            for nama, status in tugas.items():
                print(f"{nama}: {status}")

    elif pilihan == "3":
        nama = input("Masukkan nama tugas yang selesai: ")
        if nama in tugas:
            tugas[nama] = "Selesai"
            print("Tugas berhasil ditandai selesai.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "4":
        nama = input("Masukkan nama tugas yang akan dihapus: ")
        if nama in tugas:
            del tugas[nama]
            print("Tugas berhasil dihapus.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "5":
        print(f"Jumlah tugas: {len(tugas)}")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")