def palindrom(kata):
    return kata == kata[::-1]

kata = input("Masukkan sebuah kata: ")

if palindrom(kata):
    print(f"Kata {kata} merupakan palindrom.")
else:
    print(f"Kata {kata} bukan palindrom.")