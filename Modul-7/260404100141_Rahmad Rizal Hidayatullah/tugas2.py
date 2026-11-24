playlist = {}

while True:
    print("\n=== MENU PLAYLIST ===")
    print("1. Buat Playlist")
    print("2. Tambah Lagu")
    print("3. Tampilkan Playlist")
    print("4. Cari Lagu")
    print("5. Hapus Lagu")
    print("6. Hapus Playlist")
    print("7. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            print("Playlist sudah ada.")
        else:
            playlist[nama] = {}
            print("Playlist berhasil dibuat.")

    elif pilih == "2":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")

            playlist[nama][judul] = penyanyi
            print("Lagu berhasil ditambahkan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "3":
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            for nama, lagu in playlist.items():
                print("\nPlaylist:", nama)

                for judul, penyanyi in lagu.items():
                    print(judul, "-", penyanyi)

    elif pilih == "4":
        judul = input("Masukkan judul lagu: ")
        ditemukan = False

        for nama, lagu in playlist.items():
            try:
                print("Playlist:", nama)
                print("Penyanyi:", lagu[judul])
                ditemukan = True
            except KeyError:
                pass

        if ditemukan == False:
            print("Lagu tidak ditemukan.")

    elif pilih == "5":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            judul = input("Masukkan judul lagu: ")

            try:
                del playlist[nama][judul]
                print("Lagu berhasil dihapus.")
            except KeyError:
                print("Lagu tidak ditemukan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "6":
        nama = input("Masukkan playlist yang ingin dihapus: ")

        if nama in playlist:
            del playlist[nama]
            print("Playlist berhasil dihapus.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")
