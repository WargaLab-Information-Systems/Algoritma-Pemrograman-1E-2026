playlist = {}
while True:
    print("1. Buat Playlist")
    print("2. Tambah Lagu")
    print("3. Tampilkan Semua Playlist")
    print("4. Cari Lagu")
    print("5. Hapus Lagu")
    print("6. Hapus Playlist")
    print("7. Keluar")
    pilihan = input("Pilih menu (1-7): ")
    if pilihan == "1":
        nama_playlist = input("Masukkan nama playlist: ")
        if nama_playlist in playlist:
            print("Playlist sudah tersedia!")
        else:
            playlist[nama_playlist] = {}
            print("Playlist berhasil dibuat!")
    elif pilihan == "2":
        nama_playlist = input("Masukkan nama playlist: ")
        judul = input("Masukkan judul lagu: ")
        penyanyi = input("Masukkan nama penyanyi: ")
        try:
            playlist[nama_playlist][judul] = penyanyi
            print("Lagu berhasil ditambahkan!")
        except KeyError:
            print("Playlist tidak ditemukan!")
    elif pilihan == "3":
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            for nama, lagu in playlist.items():
                print("Playlist:", nama)
                if len(lagu) == 0:
                    print("Belum ada lagu.")
                else:
                    for judul, penyanyi in lagu.items():
                        print("-", judul, ":", penyanyi)
    elif pilihan == "4":
        cari = input("Masukkan judul lagu: ")
        ditemukan = False
        for nama, lagu in playlist.items():
            try:
                print("Playlist:", nama)
                print("Judul:", cari)
                print("Penyanyi:", lagu[cari])
                ditemukan = True
            except KeyError:
                pass
        if ditemukan == False:
            print("Lagu tidak ditemukan!")
    elif pilihan == "5":
        nama_playlist = input("Masukkan nama playlist: ")
        judul = input("Masukkan judul lagu: ")
        try:
            del playlist[nama_playlist][judul]
            print("Lagu berhasil dihapus!")
        except KeyError:
            print("Playlist atau lagu tidak ditemukan!")
    elif pilihan == "6":
        nama_playlist = input("Masukkan nama playlist: ")
        try:
            del playlist[nama_playlist]
            print("Playlist berhasil dihapus!")
        except KeyError:
            print("Playlist tidak ditemukan!")
    elif pilihan == "7":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")