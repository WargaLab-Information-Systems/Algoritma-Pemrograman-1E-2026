#TICKET ORDERING SYSTEM
beliminum = input("")
regular = 40.000
vip = 75.000
vvip = 100.000
pembeliantiket = 0
membercard = input("")
harga = 0
while pembeliantiket != 0:
    pelanggan = input("atas nama: ")
    print ("atas nama kakak", pelanggan, "ingin membeli jenis tiket yang mana kak?")
    tiket = input("masukkan tiket yang dipilih: ")
    if tiket == "reguler":
        while pembeliantiket != 0:
            print ("apakah ada tambahan lain kak")
            tiket = input("masukkan tiket yang dipilih:")
            break
        print ("baik kakak untuk pembelian reguler apa kakak tertarik untuk membeli minuman seharga Rp. 10.000/tiket?, ")
        beliminum = input("")
        if beliminum == "yes":
            print ("baik silahkan pilih varian minuman yang akan dipesan")
        else:
            harga += regular
            print ("baik totalnya adalah", harga)
    elif tiket == "vip" and tiket == "vvip":
        print ("selamat kakak atas pembelian tiket reguler kakak akan mendapat minuman gratis")
    elif pembeliantiket >3:
        if membercard == ada:
            print("mendapat diskon 15% menjadi", harga (harga * 0.15))
        else:
            print ("mendapar diskon sebesar 10%", harga (harga * 0.10))






    #untuk awalannya saya mendeklarasikan 



