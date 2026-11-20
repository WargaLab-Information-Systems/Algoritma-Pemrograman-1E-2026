def evaluasi_pc(status, ram):
    if int(ram) >= 8 and status == "Normal":
        return "Layak"
    else:
        return "Tidak Layak"


data_pc = []

jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("\nData PC ke-", i + 1)

    nama = input("Masukkan nama PC: ")
    status = input("Masukkan status PC: ")
    ram = input("Masukkan kapasitas RAM: ")

    data_pc.append([nama, status, ram])


print("\n=== HASIL EVALUASI PC ===")

for pc in data_pc:
    try:
        hasil = evaluasi_pc(pc[1], pc[2])

    except ValueError:
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')