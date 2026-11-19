undangan = set()
webinar_A = set()
webinar_B = set()

print("INPUT DAFTAR UNDANGAN:")
jumlah = int(input("Masukkan jumlah undangan: "))

for i in range(jumlah):
    nama = input("Nama undangan: ")
    undangan.add(nama)

print("INPUT PESERTA WEBINAR A:")
jumlah = int(input("Masukkan jumlah peserta Webinar A: "))

for i in range(jumlah):
    nama = input("Nama peserta: ")
    webinar_A.add(nama)

print("INPUT PESERTA WEBINAR: B ")
jumlah = int(input("Masukkan jumlah peserta Webinar B: "))

for i in range(jumlah):
    nama = input("Nama peserta: ")
    webinar_B.add(nama)

semua_peserta = webinar_A.union(webinar_B)

peserta_keduanya = webinar_A.intersection(webinar_B)

peserta_satu = webinar_A.symmetric_difference(webinar_B)

tidak_hadir = undangan.difference(semua_peserta)

print("HASIL DATA WEBINAR:")

print("Semua peserta kedua webinar:")
print(semua_peserta)

print("Peserta yang hadir di kedua webinar:")
print(peserta_keduanya)

print("Peserta yang hanya hadir di salah satu webinar:")
print(peserta_satu)

print("\nUndangan yang tidak hadir di webinar mana pun:")
print(tidak_hadir)