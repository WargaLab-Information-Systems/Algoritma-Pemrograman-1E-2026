asisten = []
nama = input("Nama asisten awal: ")
while nama != "cukup":
    asisten.append(nama)
    nama = input("Nama asisten awal: ")
asisten = tuple(asisten)

asisten = asisten + (input("Asisten tambahan: "),)

hari = []
h = input("Hari tugas: ")
while h != "cukup":
    hari.append(h)
    h = input("Hari tugas: ")   
hari = tuple(hari)                           

x_asisten = input("Asisten pengecualian: ")
while x_asisten not in asisten:
    print("Asisten tidak ada dalam daftar asisten.")
    x_asisten = input("Asisten pengecualian: ")
    continue
x_hari = input("Hari pengecualian: ")

for a in asisten:
    for h in hari:
        if a == x_asisten and h == x_hari:
            continue
        print(a, "-", h)