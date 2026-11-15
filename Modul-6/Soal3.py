def evaluasi(data):
    ram = int(data[2])
    if data[1].lower() == "normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"
daftar_pc = []
jumlah = int(input("Masukkan jumlah PC: "))
for i in range(jumlah):
    print("Data PC ke-", i + 1)
    nama = input("Nama PC: ")
    status = input("Status PC: ")
    ram = input("Kapasitas RAM: ")
    daftar_pc.append([nama, status, ram])
print("Hasil Evaluasi:")
for data in daftar_pc:
    try:
        hasil = evaluasi(data)
    except ValueError:
        hasil = "Format RAM Kacau"
    output = '{ "PC": "' + data[0] + '", "Status": "' + hasil + '" }'
    print(output)







