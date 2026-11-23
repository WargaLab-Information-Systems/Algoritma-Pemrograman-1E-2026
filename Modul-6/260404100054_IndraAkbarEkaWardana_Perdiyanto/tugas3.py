pc = []

jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("Data PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")

    pc.append([nama, status, ram])

def evaluasi(status, ram):

    if status == "Normal" and int(ram) >= 8:
        return "Layak"
    else:
        return "Tidak Layak"


print("Hasil Evaluasi PC:")

for data in pc:

    hasil = "Format RAM Kacau"

    if data[2].isdigit():
        hasil = evaluasi(data[1], data[2])

    print('{ "PC": "' + data[0] +
          '", "Status": "' + hasil + '" }')
