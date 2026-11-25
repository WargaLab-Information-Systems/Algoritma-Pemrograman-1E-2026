undangan = set()
webinar_a = set()
webinar_b = set()

def isi_set(himpunan, judul):
    print(f"\nMasukkan nama untuk {judul} (ketik 'selesai' untuk berhenti)")
    while True:
        nama = input("Nama: ").strip()
        if nama.lower() == "selesai":
            break
        if nama:
            himpunan.add(nama)

isi_set(undangan, "daftar undangan")
isi_set(webinar_a, "peserta Webinar A")
isi_set(webinar_b, "peserta Webinar B")

semua_peserta = webinar_a | webinar_b      
hadir_keduanya = webinar_a & webinar_b     
hanya_satu = webinar_a ^ webinar_b         
tidak_hadir = undangan - semua_peserta     

print("\n=== HASIL ===")
print("Semua peserta kedua webinar :", sorted(semua_peserta))
print("Hadir di kedua webinar      :", sorted(hadir_keduanya))
print("Hanya hadir di salah satu   :", sorted(hanya_satu))
print("Undangan tidak hadir        :", sorted(tidak_hadir))