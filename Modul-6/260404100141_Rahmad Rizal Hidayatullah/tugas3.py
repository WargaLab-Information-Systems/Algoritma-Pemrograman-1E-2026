def input_angka_positif(nomor):
    while True:
        try:
            angka = int(input(nomor))
            if angka > 0:
                return angka
            print("Angka harus lebih dari 0")
        except ValueError:
            print("Input tidak valid, Harus berupa angka")


def input_status(device):
    while True:
        status = input(device)
        if status == "Normal" or status == "Rusak":
            return status
        print("Status hanya boleh 'Normal' atau 'Rusak'. Silakan ulangi.")


def input_nama_pc(komputer):
    while True:
        nama= input(komputer)
        if nama != "":
            return nama
        print("Nama PC tidak boleh kosong")


def evaluasi_kelayakan(pc):
    ram = int(pc[2])
    if pc[1] == "Normal" and ram >= 8:
        return "Layak"
    return "Tidak Layak"


jumlah = input_angka_positif("Berapa jumlah PC yang akan didata? ")
data_pc = []
for i in range(jumlah):
    print("\nData PC ke-" + str(i + 1))
    nama = input_nama_pc("Nama PC : ")
    status = input_status("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")
    data_pc.append([nama, status, ram])

print("\n=== Hasil Evaluasi ===")
for pc in data_pc:
    try:
        hasil = evaluasi_kelayakan(pc)
    except ValueError:
        hasil = "Format RAM Kacau"
    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')