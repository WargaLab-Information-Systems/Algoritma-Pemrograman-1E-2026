undangan = set()
webinarA = set()
webinarB = set()

for nama_set, label in [(undangan, "undangan"),
                        (webinarA, "peserta webinar A"),
                        (webinarB, "epserta webinar B")]:
    while True:
        try:
            data = input(f"masukkan {label} (pisahkan dengan koma): ")
            if data == "":
                raise ValueError
            break
        except ValueError:
            print("input tidak boleh kosong, coba lagi.")

    for nama in data.split(","):
        nama_set.add(nama.strip())

print("\nsemua peserta      :", webinarA | webinarB)
print("hadir dikeduanya     :", webinarA & webinarB)
print("hanya di salah satu  :", webinarA ^ webinarB)
print("undangan tidak hadir :", undangan - (webinarA | webinarB))
