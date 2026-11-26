playlist ={}

def buat_playlist():
    nama = input("nama playlist: ")
    if not nama: 
        print("nama playlist tidak boleh kosong.")
    elif nama in playlist:
        print("playlist sudah ada.")
    else:
        playlist[nama] = {}
        print(f"playlist '{nama}' dibuat.")

def tambah_lagu():
    nama = input("nama playlist: ")
    try:
        lagu = playlist[nama]
    except KeyError:
        print(f"playlist '{nama}' tidak ditemukan.")
        return
    judul = input("judul lagu: ")
    penyanyi = input("penyanyi: ")
    if not judul or not penyanyi:
        print("judul dan penyanyi tidak boleh kosong.")
        return
    lagu[judul] = penyanyi
    print(f"lagu '{judul}' ditambahkan ke '{nama}'.")

def tampilkan_semua():
    if not playlist:
        print("belum ada playlist.")
        return
    for nama, lagu in playlist.items():
        print(f"\nplaylist: {nama}")
        if not lagu:
            print(" (kosong)")
        for i, (judul, penyanyi) in enumerate (lagu.items(), 1):
            print(f" {i}. {judul} - {penyanyi}")


def cari_lagu():
    kata = input("judul lagu yang dicari: ").lower()
    ditemukan = False
    for nama, lagu in playlist.items():
        for judul, penyanyi in lagu.items():
            if kata in judul.lower():
                print(f"'{judul}' oleh {penyanyi} ada di playlist '{nama}'")
                ditemukan = True
    if not ditemukan:
        print("lagu tidak ditemukan")

def hapus_lagu():
    nama = input("nama playlist: ")
    if nama not in playlist:
        print(f"playlist '{nama}' tidak ditemukan")
        return
    judul = input("judul lagu yang dihapus: ")
    if judul in playlist[nama]:
        del playlist[nama][judul]
        print(f"lagu '{judul}' dihapus dari '{nama}'.")
    else:
        print(f"lagu '{judul}' tidak ada di playlist '{nama}'.")


def hapus_playlist():
    nama = input("nama playlist yang ingin dihapus: ")
    try:
        del playlist[nama]
        print(f"playlist '{nama}' dihapus.")
    except KeyError:
        print(f"playlist '{nama}' tidak ditemukan.")

while True:
    print("\n=== PLAYLIST MUSIK ===")
    print("1. Buat playlist")
    print("2. Tambah lagu ke playlist")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("7. Keluar")
    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        buat_playlist()
    elif pilihan == "2":
        tambah_lagu()
    elif pilihan == "3":
        tampilkan_semua()
    elif pilihan == "4":
        cari_lagu()
    elif pilihan == "5":
        hapus_lagu()
    elif pilihan == "6":
        hapus_playlist()
    elif pilihan == "7":
        print("Terima kasih!")
        break
    else:
        print("pilihan tidak valid")