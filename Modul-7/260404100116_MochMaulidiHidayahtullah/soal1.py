# Dictionary untuk menyimpan tugas
tugas = {}


# Fungsi menampilkan tugas
def tampilkan_tugas():
    if len(tugas) == 0:
        print("Belum ada tugas.")
    else:
        print("\nDaftar Tugas:")
        for nama, status in tugas.items():
            print(nama, "-", status)


# Fungsi menghitung tugas
def hitung_tugas():
    selesai = 0
    belum = 0

    for status in tugas.values():
        if status == "Selesai":
            selesai += 1
        else:
            belum += 1

    print("Tugas selesai:", selesai)
    print("Tugas belum selesai:", belum)


# Program utama
while True:
    print("\nTO-DO LIST")
    print("1. Tambah tugas")
    print("2. Tampilkan tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Hitung status tugas")
    print("6. Keluar")

    try:
        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            while True:
                nama = input("Masukkan nama tugas: ").strip()

                if not nama.replace(" ", ""):
                    print("Nama tidak boleh kosong")
                    continue

                if nama == "udah":
                    break

                tugas[nama] = "Belum selesai"
                print(
                    "Tugas berhasil ditambahkan. Masukkan kata 'udah' untuk mengakhiri tambah tugas"
                )

        elif pilihan == 2:
            tampilkan_tugas()

        elif pilihan == 3:
            if len(tugas) == 0:
                print("Belum ada tugas.")
            else:
                nama = input("Masukkan nama tugas: ").strip()

                while nama == "" or nama not in tugas:
                    print("Nama tugas kosong atau tidak ditemukan.")
                    nama = input("Masukkan nama tugas lagi: ").strip()

                tugas[nama] = "Selesai"
                print("Tugas berhasil diselesaikan.")

        elif pilihan == 4:
            if len(tugas) == 0:
                print("Belum ada tugas.")
            else:
                nama = input("Masukkan nama tugas: ").strip()

                while nama == "" or nama not in tugas:
                    print("Nama tugas kosong atau tidak ditemukan.")
                    nama = input("Masukkan nama tugas lagi: ").strip()

                del tugas[nama]
                print("Tugas berhasil dihapus.")

        elif pilihan == 5:
            hitung_tugas()

        elif pilihan == 6:
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")

    except ValueError:
        print("Input harus berupa angka.")
