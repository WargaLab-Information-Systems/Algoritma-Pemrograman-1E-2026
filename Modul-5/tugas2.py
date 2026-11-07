kata = input("Masukkan kata : ")

def palindrom(kata):
    balik = ""

    for i in range(len(kata) -1, -1, -1):
        balik = balik + kata[i]

    print("Kata setelah dibalik :", balik)

    if kata == balik:
        return True
    else :
        return False

hasil = palindrom(kata)

if hasil == True :
    print(kata, "adalah kata palindrom")
else :
    print(kata, "bukan kata palindrom")