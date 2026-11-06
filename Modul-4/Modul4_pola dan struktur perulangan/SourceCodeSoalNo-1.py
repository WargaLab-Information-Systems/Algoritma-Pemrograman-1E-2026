BarisLampu = int(input("masukkan baris lampu:"))
JumlahLampu = int(input("masukkan jumlah lampu:"))

for Baris in range(1,BarisLampu + 1):
    print(f"jumlah lampu pada baris ke-{Baris} adalah:")
    for Lampu in range(1,JumlahLampu + 1):
        if Lampu % 3 == 0:
            print(f"Lampu ke-{Lampu} mengalami gangguan")
        else:
            print(f"Lampu ke-{Lampu} normal")
print("==periksalah sumber listrik utama taman==")