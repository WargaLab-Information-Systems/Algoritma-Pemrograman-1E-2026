# Program Menghitung Kebutuhan BBM Dimas
jarakPergi = 100
jarakPulangPergi = jarakPergi * 2

konsumsiBBM = 40
sisaBBM = 1.5
hargaBBM = 10000

kebutuhanBBM = jarakPulangPergi / konsumsiBBM
bbmDibeli = kebutuhanBBM - sisaBBM
totalHargaBBM = bbmDibeli * hargaBBM

print(f"Total jarak pulang-pergi =  {jarakPulangPergi} km")
print("Kebutuhan BBM = ", kebutuhanBBM, "liter")
print("BBM yang dibeli = ", bbmDibeli, "liter")
print("Total harga BBM = Rp", totalHargaBBM)