playlist = {}

while True:
    print("MENU PLAYLIST")
    print("1. Membuat playlist lagu")
    print("2. Menambahkan lagu ke playlist")
    print("3. Menampilkan semua playlist")
    print("4. Mencari lagu dalam playlist")
    print("5. Menghapus lagu dari playlist")
    print("6. Menghapus playlist")
    print("7. Keluar")
    pilihan = input("Masukkan pilihan (1-7): ")
    
    if pilihan == "1":
        nama_playlist = input("Masukkan nama playlist: ")
        if nama_playlist in playlist:
            print("Playlist sudah ada.")
        else:
            playlist[nama_playlist] = {}
            print("Playlist berhasil dibuat.")
            
    elif pilihan == "2":
        nama_playlist = input("Masukkan nama lagu playlist: ")
        try:
            playlist[nama_playlist]

            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")

            if judul in playlist[nama_playlist]:
                print("Lagu sudah tersedia!")
            else:
                playlist[nama_playlist][judul] = penyanyi
                print("Lagu berhasil ditambahkan!")

        except KeyError:
            print("Playlist tidak ditemukan!")

    elif pilihan == "3":
        if len(playlist) == 0:
            print("Belum ada playlist!")
        else:
            print("DAFTAR PLAYLIST:")

            for nama_playlist, lagu in playlist.items():
                print("\nPlaylist:", nama_playlist)

                if len(lagu) == 0:
                    print("Belum ada lagu!")
                else:
                    for judul, penyanyi in lagu.items():
                        print(judul, "-", penyanyi)

    elif pilihan == "4":
        cari = input("Masukkan judul lagu: ")

        ditemukan = False

        for nama_playlist, lagu in playlist.items():
            if cari in lagu:
                print("\nLagu ditemukan!")
                print("Judul lagu :", cari)
                print("Penyanyi   :", lagu[cari])
                print("Playlist   :", nama_playlist)

                ditemukan = True

        if ditemukan == False:
            print("Lagu tidak ditemukan!")

    elif pilihan == "5":
        nama_playlist = input("Masukkan nama playlist: ")

        try:
            playlist[nama_playlist]

            judul = input("Masukkan judul lagu yang dihapus: ")

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
        print("Terima kasih telah menggunakan program playlist musik!")
        break

    else:
        print("Pilihan tidak valid!")