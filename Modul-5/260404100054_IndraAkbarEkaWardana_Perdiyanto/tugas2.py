def palindrom(kata):
    balik = ""
    for huruf in kata:
        balik = huruf + balik
    if kata == balik:
        return True
    else:
        return False

kata = input("Masukkan sebuah kata: ")
if palindrom(kata):
    print(kata, "adalah palindrom")
else:
    print(kata, "bukan palindrom")
