tugas = {}

while True:
    print("MENU TO-DO LIST")
    print("1. Tambah Tugas")
    print("2. Tampilkan Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas Selesai dan Belum")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama tugas: ")

        if nama in tugas:
            print("Tugas sudah ada!")
        else:
            tugas[nama] = "Belum Selesai"
            print("Tugas berhasil ditambahkan!")

    elif pilihan == "2":
        print("DAFTAR TUGAS")

        if len(tugas) == 0:
            print("Belum ada tugas.")
        else:
            for nama in tugas:
                print(nama, "-", tugas[nama])

    elif pilihan == "3":
        nama = input("Masukkan nama tugas: ")

        try:
            tugas[nama] = "Selesai"
            print("Tugas berhasil diselesaikan!")
        except:
            print("Terjadi kesalahan!")

        if nama not in tugas:
            print("Tugas tidak ditemukan!")

    elif pilihan == "4":
        nama = input("Masukkan nama tugas: ")

        try:
            del tugas[nama]
            print("Tugas berhasil dihapus!")
        except KeyError:
            print("Tugas tidak ditemukan!")


    elif pilihan == "5":
        selesai = 0
        belum = 0

        for nama in tugas:
            if tugas[nama] == "Selesai":
                selesai = selesai + 1
            else:
                belum = belum + 1

        print("Tugas selesai:", selesai)
        print("Tugas belum selesai:", belum)

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
