def palindrom(kata):
    return kata == kata[::-1]

kata = input("Masukkan sebuah kata: ").lower()
hasil = palindrom(kata)

print("Hasil fungsi:", hasil)
if hasil:
    print(f'Kata "{kata}" adalah palindrom')
else:
    print(f'Kata "{kata}" bukan palindrom')