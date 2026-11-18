reguler = 40000
vip = 75000
vvip = 100000
harga = 0
tiket = 0
# menanayakan apakah ingin beli tiket
while True:
    input("beli tiket? masukan harga : ")
    tiket += 1
        # cek harga jika 40000 maka ter golong reguler, jika 75k atau 100k maka vip/vvip
    if  input == 75000 or input == 100000:
        print("dapat free minuman")
    if input == 40000:
        # tanya apakah mau tambah minum
        input.lower("mau tambah minum? harganya 10000")
        if input == "y":
            print("tambah minum")
        else:
            continue
    elif tiket == 3:
        input("ada member card?")
        if input == "ada":
            ()

    else:
        break
                
        
        
    
    
