# Dictionary untuk menyimpan playlist
playlist = {}


# Fungsi menampilkan semua playlist
def tampilkan_playlist():
    if len(playlist) == 0:
        print("Belum ada playlist.")
    else:
        for nama, lagu in playlist.items():
            print("\nPlaylist:", nama)

            if len(lagu) == 0:
                print("Belum ada lagu.")
            else:
                for judul, penyanyi in lagu.items():
                    print(judul, "-", penyanyi)


# Fungsi mencari lagu
def cari_lagu():
    if len(playlist) == 0:
        print("Belum ada playlist.")
    else:
        judul = input("Masukkan judul lagu: ").strip()

        while judul == "":
            print("Judul lagu tidak boleh kosong.")
            judul = input("Masukkan judul lagu lagi: ").strip()

        ditemukan = False

        for nama, lagu in playlist.items():
            if judul in lagu:
                print("Lagu ditemukan di playlist:", nama)
                print("Penyanyi:", lagu[judul])
                ditemukan = True

        while not ditemukan:
            print("Lagu tidak ditemukan.")
            judul = input("Masukkan judul lagu lagi: ").strip()

            while judul == "":
                print("Judul lagu tidak boleh kosong.")
                judul = input("Masukkan judul lagu lagi: ").strip()

            for nama, lagu in playlist.items():
                if judul in lagu:
                    print("Lagu ditemukan di playlist:", nama)
                    print("Penyanyi:", lagu[judul])
                    ditemukan = True


# Program utama
while True:
    print("\nPLAYLIST MUSIK")
    print("1. Buat playlist")
    print("2. Tambah lagu")
    print("3. Tampilkan playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu")
    print("6. Hapus playlist")
    print("7. Keluar")

    try:
        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            nama = input("Masukkan nama playlist: ").strip()

            while nama == "":
                print("Nama playlist tidak boleh kosong.")
                nama = input("Masukkan nama playlist lagi: ").strip()

            if nama not in playlist:
                playlist[nama] = {}
                print("Playlist berhasil dibuat.")
            else:
                print("Playlist sudah tersedia.")

        elif pilihan == 2:
            if len(playlist) == 0:
                print("Belum ada playlist. Buat playlist terlebih dahulu.")
            else:
                nama = input("Masukkan nama playlist: ").strip()

                while nama == "" or nama not in playlist:
                    print("Nama playlist kosong atau tidak ditemukan.")
                    nama = input("Masukkan nama playlist lagi: ").strip()

                judul = input("Masukkan judul lagu: ").strip()

                while judul == "":
                    print("Judul lagu tidak boleh kosong.")
                    judul = input("Masukkan judul lagu lagi: ").strip()

                penyanyi = input("Masukkan nama penyanyi: ").strip()

                while penyanyi == "":
                    print("Nama penyanyi tidak boleh kosong.")
                    penyanyi = input("Masukkan nama penyanyi lagi: ").strip()

                playlist[nama][judul] = penyanyi
                print("Lagu berhasil ditambahkan.")

        elif pilihan == 3:
            tampilkan_playlist()

        elif pilihan == 4:
            cari_lagu()

        elif pilihan == 5:
            if len(playlist) == 0:
                print("Belum ada playlist.")
            else:
                nama = input("Masukkan nama playlist: ").strip()

                while nama == "" or nama not in playlist:
                    print("Playlist kosong atau tidak ditemukan.")
                    nama = input("Masukkan nama playlist lagi: ").strip()

                if len(playlist[nama]) == 0:
                    print("Playlist belum memiliki lagu.")
                else:
                    judul = input("Masukkan judul lagu: ").strip()

                    while judul == "" or judul not in playlist[nama]:
                        print("Judul lagu kosong atau tidak ditemukan.")
                        judul = input("Masukkan judul lagu lagi: ").strip()

                    del playlist[nama][judul]
                    print("Lagu berhasil dihapus.")

        elif pilihan == 6:
            if len(playlist) == 0:
                print("Belum ada playlist.")
            else:
                nama = input("Masukkan nama playlist: ").strip()

                while nama == "" or nama not in playlist:
                    print("Playlist kosong atau tidak ditemukan.")
                    nama = input("Masukkan nama playlist lagi: ").strip()

                del playlist[nama]
                print("Playlist berhasil dihapus.")

        elif pilihan == 7:
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")

    except ValueError:
        print("Input harus berupa angka.")
