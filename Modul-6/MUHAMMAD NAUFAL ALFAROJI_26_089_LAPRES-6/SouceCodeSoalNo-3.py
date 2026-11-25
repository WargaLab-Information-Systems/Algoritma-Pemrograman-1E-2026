inventaris = []

jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("\nData PC ke-", i + 1)

    nama = input("Masukkan nama PC: ")
    status = input("Masukkan status PC (Normal/Rusak): ")
    ram = input("Masukkan kapasitas RAM (GB): ")

    inventaris.append([nama, status, ram])

def evaluasi_pc(status, ram):
    kapasitas = int(ram)

    if status == "Normal" and kapasitas >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

print("\n=== HASIL EVALUASI INVENTARIS ===")

for pc in inventaris:
    try:
        hasil = evaluasi_pc(pc[1], pc[2])

    except ValueError:
        hasil = "Format RAM Kacau"

    output = '{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }'

    print(output)
