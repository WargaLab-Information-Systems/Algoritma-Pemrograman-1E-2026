def cek_pc(status, ram):
    if int(ram) >= 8 and status == "normal":
        return "Layak"
    else:
        return "Tidak Layak"


data_pc = []

while True:
    try:
        jumlah = int(input("Masukkan jumlah PC: "))

        if jumlah > 0:
            break

        print("Jumlah harus lebih dari 0!")

    except ValueError:
        print("Masukkan angka yang benar!")


for i in range(jumlah):
    print("\nData PC ke-", i + 1)

    while True:
        nama = input("Nama PC: ").strip()

        if nama != "":
            break

        print("Nama PC tidak boleh kosong!")

    while True:
        status = input("Status PC (Normal/Rusak): ").lower()

        if status == "normal" or status == "rusak":
            break

        print("Status tidak valid!")

    while True:
        ram = input("Kapasitas RAM: ")

        if ram.lstrip("-").isdigit():
            if int(ram) >= 0:
                break

            print("RAM tidak boleh negatif!")
        else:
            break

    data_pc.append([nama, status, ram])


print("\nHasil Evaluasi PC")

for pc in data_pc:
    try:
        hasil = cek_pc(pc[1], pc[2])

    except ValueError:
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')
