def evaluasi_pc(status, ram):
    if status.lower() == "normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"
    
jumlah = int(input("Masukkan jumlah PC: "))
inventaris = []

for i in range(jumlah):
    print(f"Data PC ke-{i + 1}")
    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")
    inventaris.append([nama, status, ram])

print("evaluasi PC:")
for pc in inventaris:
    try:
        hasil = evaluasi_pc(pc[1], int(pc[2]))
    except ValueError:
        hasil = "Format RAM Kacau"
    output = "{ 'PC': '" + pc[0] + "', 'Status': '" + hasil + "' }"
    print(f'PC : {pc[0]}, status {hasil}')
    print(output)