playlists = {}  

while True:
    print("\n=== PENGELOLA PLAYLIST MUSIK ===")
    print("1. Buat playlist")
    print("2. Tambah lagu ke playlist")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("0. Keluar")

    try:
        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            nama = input("Nama playlist: ").strip()
            if nama == "":
                raise ValueError("Nama playlist tidak boleh kosong.")
            if nama in playlists:
                raise ValueError("Playlist sudah ada.")
            playlists[nama] = {}
            print(f"Playlist '{nama}' dibuat.")

        elif pilih == "2":
            nama = input("Nama playlist: ").strip()
            judul = input("Judul lagu: ").strip()
            penyanyi = input("Penyanyi: ").strip()
            if judul == "" or penyanyi == "":
                raise ValueError("Judul dan penyanyi tidak boleh kosong.")
            playlists[nama][judul] = penyanyi  
            print(f"Lagu '{judul}' ditambahkan ke '{nama}'.")

        elif pilih == "3":
            if not playlists:
                print("Belum ada playlist.")
            for nama, lagu in playlists.items():
                print(f"\nPlaylist: {nama}")
                if not lagu:
                    print("  (kosong)")
                for judul, penyanyi in lagu.items():
                    print(f"  - {judul} | {penyanyi}")

        elif pilih == "4":
            kata = input("Judul lagu yang dicari: ").strip().lower()
            ketemu = False
            for nama, lagu in playlists.items():
                for judul, penyanyi in lagu.items():
                    if kata in judul.lower():
                        print(f"'{judul}' oleh {penyanyi} ada di playlist '{nama}'")
                        ketemu = True
            if not ketemu:
                print("Lagu tidak ditemukan.")

        elif pilih == "5":
            nama = input("Nama playlist: ").strip()
            judul = input("Judul lagu yang dihapus: ").strip()
            del playlists[nama][judul] 
            print(f"Lagu '{judul}' dihapus dari '{nama}'.")

        elif pilih == "6":
            nama = input("Nama playlist yang dihapus: ").strip()
            del playlists[nama] 
            print(f"Playlist '{nama}' dihapus.")

        elif pilih == "0":
            print("Terima kasih!")
            break

        else:
            print("Menu tidak valid.")

    except KeyError:
        print("Error: playlist atau lagu yang dituju tidak ditemukan.")

