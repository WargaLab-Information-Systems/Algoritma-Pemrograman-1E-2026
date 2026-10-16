suhu = int(input("masukkan suhu: "))
tekanan = int(input("masukkan tekanan: "))

if suhu >1000:
    if tekanan >50:
        print ("MELTDOWN!SEGERA EVAKUASI!")
    if tekanan <=50:
        print ("Bahaya suhu: Segera Turunkan Daya!")
elif suhu >500 <=1000:
    if tekanan >30:
        print ("Tekanan Tidak Stabil")
    else:
        print ("Operasi Reaktor Normal")
else:
    print ("Reaktor Belum Panas")


StatusOperasionalPompaAir = "Pompa Maksimal" if suhu >800 else "Pompa Normal"
print (StatusOperasionalPompaAir)