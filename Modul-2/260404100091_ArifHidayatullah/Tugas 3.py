suhu = float(input("masukkan suhu reaktor (celcius): "))
tekanan = float(input("masukkan tekanan gas (bar): "))

if suhu > 1000:
    if tekanan > 50:
        status_bahaya = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status_bahaya = "Bahaya Suhu: Segera Turunkan Daya"
elif suhu > 500:
    if tekanan > 30:
        status_bahaya = "Tekanan Tidak Stabil"
    else:
        status_bahaya = "Operasi Reaktor Normal"
else:
    status_bahaya = "Reaktor Belum Cukup Panas"

status_pompa = ("Pompa Maksimal" if suhu > 800 else "Pompa Normal")

print("\n" + "=" * 45)
print("LAPORAN PEMANTAUAN REAKTOR NUKLIR")
print("=" * 45)
print(f"Suhu Reaktor : {suhu}C")
print(f"Tekanan Gas : {tekanan} Bar")
print(f"Pesan Bahaya : {status_bahaya}")
print(f"Status Pompa : {status_pompa}")
print("=" * 45)
