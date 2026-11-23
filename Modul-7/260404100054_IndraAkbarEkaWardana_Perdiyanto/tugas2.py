playlist = {}

while True:
    print("MENU PLAYLIST MUSIK")
    print("1. Buat Playlist")
    print("2. Tambah Lagu")
    print("3. Tampilkan Playlist")
    print("4. Cari Lagu")
    print("5. Hapus Lagu")
    print("6. Hapus Playlist")
    print("7. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            print("Playlist sudah ada!")
        else:
            playlist[nama] = {}
            print("Playlist berhasil dibuat!")

    elif pilihan == "2":
        nama = input("Masukkan nama playlist: ")

        try:
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")

            playlist[nama][judul] = penyanyi
            print("Lagu berhasil ditambahkan!")

        except KeyError:
            print("Playlist tidak ditemukan!")

    elif pilihan == "3":
        print("DAFTAR PLAYLIST")

        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            for nama in playlist:
                print("Playlist:", nama)

                if len(playlist[nama]) == 0:
                    print("Belum ada lagu.")
                else:
                    for judul in playlist[nama]:
                        print(judul, "-", playlist[nama][judul])

    elif pilihan == "4":
        cari = input("Masukkan judul lagu: ")
        ditemukan = False

        for nama in playlist:
            if cari in playlist[nama]:
                print("Lagu ditemukan!")
                print("Playlist:", nama)
                print("Penyanyi:", playlist[nama][cari])
                ditemukan = True

        if ditemukan == False:
            print("Lagu tidak ditemukan!")

    elif pilihan == "5":
        nama = input("Masukkan nama playlist: ")

        try:
            judul = input("Masukkan judul lagu: ")
            del playlist[nama][judul]
            print("Lagu berhasil dihapus!")

        except KeyError:
            print("Playlist atau lagu tidak ditemukan!")

    elif pilihan == "6":
        nama = input("Masukkan nama playlist: ")

        try:
            del playlist[nama]
            print("Playlist berhasil dihapus!")

        except KeyError:
            print("Playlist tidak ditemukan!")

    elif pilihan == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
