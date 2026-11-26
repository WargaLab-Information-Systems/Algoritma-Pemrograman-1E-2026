pin = int(input("masukkan pin: "))
jamKedatangan = float(input("masukkan jam kedatangan: "))

digit1 = (pin // 100)
print ("digit pertama adalah", digit1)
digit2 = ((pin // 10) % 10)
print ("digit kedua adalah", digit2)
digit3 = (pin % 10)
print ("digit ketiga adalah", digit3)

if pin % 5 == 0:
    if jamKedatangan <12.00:
        print ("Garasi Pagi Terbuka")
    else:
        print("Garasi Malam Terbuka")
        print ("Lampu Dinyalakan")
elif pin % 5 != 0 and pin % 2 == 0:
    if digit1 + digit3 == digit2:
        print ("Garasi VIP Terbuka Khusus Bos")
    else:
        print ("Kode Genap Ditolak, Alarm Berbunyi")
else:
    print ("Akses Ditolak")

StatusCCTV = "Mode Malam Merekam" if jamKedatangan >18.00 else "Mode Siang Standby"
print (StatusCCTV)