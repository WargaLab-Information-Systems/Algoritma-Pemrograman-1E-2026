undangan = set()
webinar_a = set()
webinar_b = set()

print("=== DATA UNDANGAN ===")
jumlah = int(input("Masukkan jumlah undangan: "))

for i in range(jumlah):
    nama = input("Masukkan nama undangan: ")
    undangan.add(nama)

print("\n=== PESERTA WEBINAR A ===")
jumlah = int(input("Masukkan jumlah peserta: "))

for i in range(jumlah):
    nama = input("Masukkan nama peserta: ")
    webinar_a.add(nama)

print("\n=== PESERTA WEBINAR B ===")
jumlah = int(input("Masukkan jumlah peserta: "))

for i in range(jumlah):
    nama = input("Masukkan nama peserta: ")
    webinar_b.add(nama)

semua_peserta = webinar_a | webinar_b
kedua_webinar = webinar_a & webinar_b
satu_webinar = webinar_a ^ webinar_b
tidak_hadir = undangan - semua_peserta

print("\n=== HASIL DATA WEBINAR ===")

print("Semua peserta:", semua_peserta)
print("Hadir di kedua webinar:", kedua_webinar)
print("Hadir di salah satu webinar:", satu_webinar)
print("Undangan yang tidak hadir:", tidak_hadir)
