daftar = []
nama = input("masukkan nama: ")
while True:
    if daftar != []:
         nama = input("masukkan nama: ")
    if nama in daftar:
            print("nama sudah ada")
            continue
    if nama == "selesai":
        break
    daftar.append(nama)
    

for nama in daftar:
    if nama == "admin" or len(nama) <4:
        print (f"nama {nama} tidak valid") 

penyusup = input("\nmasukkan nama yang dicurigai: ")
if penyusup in daftar:
    daftar.remove(penyusup)
    print (f"\n{penyusup} berhasil dihapus")
else:
    print (f"\n{penyusup} tidak ditemukan")

print(f"\ndaftar akhir", daftar)