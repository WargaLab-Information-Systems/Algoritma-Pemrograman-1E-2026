pin = int(input("masukkan 3 digit kode pin : "))
Jam = int(input("Masukkan jam kedatangan (format 0-23): "))

digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

if pin % 5 == 0:
    if Jam < 12:
        status_garasi = "Garasi Pagi Terbuka"
    else:
        status_garasi = "Garasi Malam Terbuka,Lampu Dinyalakan"
elif pin % 2 == 0:
    if (digit1 + digit3) == digit2:
        status_garasi = "Garasi VIP terbuka Untuk Bos"
    else:
        status_garasi = "Kode Genap Ditolak,Alarm Berbunyi!"
else:
    status_garasi = "Akses Ditolak Sepenuhnya"

status_cctv =("Mode Malam Merekam" if Jam > 18 else "Mode Siang Stanby")
print("\n" + "=" * 50)
print("HASIL EVALUASI AKSES MARKAS CIA")
print(f"PIN yang Dimasukkan : {pin}")
print(f"Jam Kedatangan  : {Jam}:00")
print(f"Digit Pertama : {digit1}")
print(f"Digit Kedua : {digit2}")
print(f"Digit Ketiga : {digit3}")
print(f"Status Pintu Garasi : {status_garasi}")
print(f"Status Kamera CCTV : {status_cctv}")
print("=" * 50)