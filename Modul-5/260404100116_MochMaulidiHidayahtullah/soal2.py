def palindrom(kata):
    balik = ""

    for huruf in kata:
        balik = huruf + balik

    if kata == balik:
        return True
    else:
        return False


kata = input("Masukkan kata: ").lower()

if palindrom(kata):
    print("Palindrom")
else:
    print("Bukan palindrom")
