tugas = {}

def tambah_tugas():
    nama = input("nama tugas: ")
    if not nama:
        print("nama tugas tidak boleh kosong.")
    elif nama in tugas:
        print("tugas sudah ada.")
    else:
        tugas[nama] = "belum selesai"
        print(f"tugas '{nama}' ditambahkan.")

def tampilkan_tugas():
    if not tugas:
        print("belum ada tugas.")
        return
    for i, (nama, status) in enumerate (tugas.items(), 1):
        print(f"{i}. {nama} - {status}")

def tandai_selesai():
    nama = input("nama tugas yang selesai: ")
    if nama in tugas:
        tugas[nama] = "selesai"
        print(f"tugas '{nama}' ditandai selesai")
    else:
        print(f"tugas '{nama}' tidak ditemukan.")

def hapus_tugas():
    nama = input("nama tugas yang dihapus: ")
    try:
        del tugas[nama]
        print(f"tugas '{nama}' dihapus.")
    except KeyError:
        print(f"tugas '{nama}' tidak ditemukan.")

def tampilkan_jumlah():
    selesai = sum(1 for s in tugas.values() if s == "selesai")
    for o, (nama) in enumerate (tugas.items(), 1):
            print(f"{o}. {nama}")
    

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas selesai & belum")
    print("6. Keluar")
    pilihan = input("pilih menu (1-6): ")

    if pilihan == "1":
        tambah_tugas()
    elif pilihan == "2":
        tampilkan_tugas()
    elif pilihan == "3":
        tandai_selesai()
    elif pilihan == "4":
        hapus_tugas()
    elif pilihan == "5":
        tampilkan_jumlah()
    elif pilihan == "6":
        print("Terima kasih!")
        break
    else:
        print("pilihan tidak valid.")