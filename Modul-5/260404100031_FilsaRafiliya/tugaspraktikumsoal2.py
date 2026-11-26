def palindrom (kata):
    kebalikan = ""
    for huruf in kata:
        kebalikan = huruf + kebalikan 
        
    if kata == kebalikan:
        return True
    else:
        return False

kata = input("masukkan kata: ")
hasil = palindrom(kata)

if hasil:
    print (f"kata {kata} adalah palindrom")
else:
    print (f"kata {kata} bukan palindrom")