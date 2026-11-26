def cek_layak (pc):
    ram = int(pc[2])
    if pc[1] == "normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

data = []

jumlah = int(input("masukkan berapa banyak PC yang akan diinput: "))
for spesifikasi in range (jumlah):
    nama = input("masukkan nama PC: ")
    status = input("masukkan status PC: ")
    ram = input("masukkan RAM PC nya: ")
    data.append([nama, status, ram])

for pc in data:
    try:
        hasil = cek_layak (pc)
    except ValueError:
        hasil = "Format RAM kacau"
    print('\n{"PC": "' + pc[0] + '", "Status": "' + hasil + '" }')