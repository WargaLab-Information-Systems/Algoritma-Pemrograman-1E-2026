#Variabel

pelanggan = input("anda mau beli? y/n ")
Reguler = 1
VIP = 2
VVIP = 3
#kondisi
while pelanggan == "y":
    print(" 1 = reguler, 2 = VIP, 3 = VVIP")
    pelanggan = input(" beli yang mana?")
    if pelanggan == 1:
        print(" anda membeli tiket reguler")
    elif pelanggan == 2:
        print(" anda membeli tiket VIP")
    elif pelanggan == 3:
        print("anda membeli tiket VVIP")       
else:
    print("input anda salah")     

Reguler = 40000
VIP = 75000
VVIP = 100000    
