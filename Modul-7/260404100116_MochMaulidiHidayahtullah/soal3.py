# Membuat tiga set kosong
undangan = set()
webinar_A = set()
webinar_B = set()


# Fungsi mengisi data peserta
def isi_data(data, nama):
    try:
        jumlah = int(input("Masukkan jumlah " + nama + ": "))

        while jumlah < 0:
            print("Jumlah tidak boleh negatif.")
            jumlah = int(input("Masukkan jumlah " + nama + ": "))

        for i in range(jumlah):
            peserta = input("Masukkan nama peserta: ").strip()

            while peserta == "":
                print("Nama tidak boleh kosong.")
                peserta = input("Masukkan nama peserta lagi: ").strip()

            data.add(peserta)

    except ValueError:
        print("Jumlah harus berupa angka.")
        isi_data(data, nama)


# Mengisi ketiga set
print("DATA UNDANGAN")
isi_data(undangan, "undangan")

print("\nPESERTA WEBINAR A")
isi_data(webinar_A, "peserta Webinar A")

print("\nPESERTA WEBINAR B")
isi_data(webinar_B, "peserta Webinar B")


# Menampilkan hasil operasi himpunan
print("\nHASIL DATA WEBINAR")

print("\nSemua peserta:")
print(webinar_A | webinar_B)

print("\nPeserta yang hadir di kedua webinar:")
print(webinar_A & webinar_B)

print("\nPeserta yang hanya hadir di salah satu webinar:")
print(webinar_A ^ webinar_B)

print("\nUndangan yang tidak hadir di webinar mana pun:")
print(undangan - (webinar_A | webinar_B))
