pin = int(input("Masukkan kode: "))
jam = int(input("masukan jam(0-23):"))
digit1 = pin //100
digit2 = (pin //10) % 10
digit3 = pin % 10

print(f"digit pertama: {digit1}, digit kedua: {digit2}, digit ketiga: {digit3}")
if pin % 5 == 0:
    if jam > 12:
        print("Garasi pagi terbuka")
    else:
        print("Garasi malam terbuka")
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        print("Garasi VIP khusus terbuka")
    else:
        print("kode ditolak, alarm berbunyi!")
else:
    print("Akses ditolak")
status_cctv = "Mode malam aktif" if jam > 18 else "Mode siang standby"
print(status_cctv)