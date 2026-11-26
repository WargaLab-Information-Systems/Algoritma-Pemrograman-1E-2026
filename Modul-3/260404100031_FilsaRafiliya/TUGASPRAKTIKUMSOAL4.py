mahasiswa = 0
kuotaPenuh = 0

while mahasiswa != 10:
    nama = input("masukkan nama: ")
    IPK = float(input("masukkan IPK: "))
    if IPK < 3.00: 
        print ("mohon maaf", nama, " kamu tidak memenuhi syarat beasiswa")
        continue
    penghasilan = int(input("masukkan penghasilan orang tua: "))
    if penghasilan <=3000000:
        print("selamat", nama, "kamu mendapat besiswa penuh")
        kuotaPenuh += 1
        if kuotaPenuh == 3:
            print ("kuota beasiswa penuh sudah terpenuhi")
            break
    elif penghasilan >3000000 and penghasilan <5000000:
        print ("selamat", nama, "kamu mendapat beasiswa sebagian")
    else:
        print("mohon maaf", nama, "kamu tidak bisa mendapatkan beasiswa")
    







