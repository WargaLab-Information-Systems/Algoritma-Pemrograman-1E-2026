undangan = set()
webinar_a = set()
webinar_b = set()
def input_jumlah(pesan):
    while True:
        try:
            jumlah = int(input(pesan))

            if jumlah < 0:
                print("Jumlah tidak boleh negatif!")
            else:
                return jumlah

        except ValueError:
            print("Input harus berupa angka bulat!")

def input_nama(pesan, data):
    while True:
        nama = input(pesan)

        if nama == "":
            print("Nama tidak boleh kosong!")
        elif nama in data:
            print("Nama sudah terdaftar! Masukkan nama lain.")
        else:
            return nama

print("== DATA UNDANGAN ==")
jumlah = input_jumlah("Masukkan jumlah undangan: ")

for i in range(jumlah):
    print("Undangan ke-", i + 1)
    nama = input_nama("Nama undangan: ", undangan)
    undangan.add(nama)

print("\n=== PESERTA WEBINAR A ===")
jumlah = input_jumlah("Masukkan jumlah peserta: ")

for i in range(jumlah):
    print("Peserta ke-", i + 1)
    nama = input_nama("Nama peserta: ", webinar_a)
    webinar_a.add(nama)

print("\n=== PESERTA WEBINAR B ===")
jumlah = input_jumlah("Masukkan jumlah peserta: ")

for i in range(jumlah):
    print("Peserta ke-", i + 1)
    nama = input_nama("Nama peserta: ", webinar_b)
    webinar_b.add(nama)


semua_peserta = webinar_a | webinar_b

peserta_keduanya = webinar_a & webinar_b

peserta_satu = webinar_a - webinar_b

tidak_hadir = undangan - semua_peserta

print("\n=== HASIL WEBINAR ===")
print("Semua peserta:", semua_peserta)
print("Peserta kedua webinar:", peserta_keduanya)
print("Peserta hanya satu webinar:", peserta_satu)
print("Undangan tidak hadir:", tidak_hadir)
