def palindrom(kata):
    balik = kata[::-1]

    if kata == balik:
        return True
    else:
        return False



print("PROGRAM CEK KATA PALINDROM")


while True:
    kata = input("Masukkan sebuah kata: ").strip()
    if kata == "":
        print("Kata tidak boleh kosong.")

    elif not kata.isalpha():
        print("input harus berupa huruf saja.")
        print("Tidak boleh menggunakan angka atau spasi.")
    else:
        break

hasil = palindrom(kata)
print("\n========== HASIL PEMERIKSAAN ==========")
print("Kata yang dimasukkan :", kata)

if hasil == True:
    print("Status               : PALINDROM")
    print("Keterangan           : Kata dibaca sama")
    print("                       dari depan maupun belakang.")
else:
    print("Status               : BUKAN PALINDROM")
    print("Keterangan           : Kata dibaca berbeda")
    print("                       dari depan maupun belakang.")


