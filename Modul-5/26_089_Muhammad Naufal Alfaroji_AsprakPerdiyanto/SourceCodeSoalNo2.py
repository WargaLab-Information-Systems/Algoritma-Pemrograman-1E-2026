
def palindrom(kata):
    kata_balik = ""
    for huruf in kata:
        kata_balik = huruf + kata_balik
    if kata == kata_balik:
        return True
    else:
        return False

kata = input("Masukkan sebuah kata: ").lower()
hasil = palindrom(kata)
print("Hasil:", hasil)
if hasil == True:
    print("Kata tersebut merupakan palindrom")
else:
    print("Kata tersebut bukan palindrom")