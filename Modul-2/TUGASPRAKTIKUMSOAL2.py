#diskon supermarket koperasi ndeso

totalBelanjaan = float(input("total belanjaan: "))

if totalBelanjaan >=100.000 and totalBelanjaan % 100.000 == 0:
    print ("dikarenakan total belanjaan anad memenuhi syarat kelipatan 100, maka anda mendapat diskon sebesar 100%, jadi total belanjaannya adalah", totalBelanjaan)
elif totalBelanjaan >=50.000 and totalBelanjaan % 50.000 == 0:
    print ("dikarenakan total belanjaan anda memenuhi syarat keliapatan 50, selamat anda mendapat diskon sebesar 50%, jadi total belanjaannya adalah", totalBelanjaan - (totalBelanjaan * 0.50))
elif totalBelanjaan >=10.000 and totalBelanjaan % 10.000 == 0:
    print ("dikarenakan total belanjaann anda memenuhi syarat kelipatan 10, selamat anda mendapat diskon sebesar 20%, jadi total belanjaannya adalah", totalBelanjaan - (totalBelanjaan * 0.20))
elif totalBelanjaan >200.000 and totalBelanjaan / 10.000 != 0:
    print ("dikarenakan belanjaan anda lebih dari 200.000, selamat anda mendapat diskon sebesar 10%, jadi total belanjannya adalah", totalBelanjaan - (totalBelanjaan * 0.10))
else:
    print ("mohon maaf ibu dikarenakan anda tidak memenuhi syarat diskon dari toko kami, maka anda akan membayar dengan harga normal, totalnya adalah", totalBelanjaan)


poin = "tidak ada poin" if totalBelanjaan >=100.000 and totalBelanjaan % 100.000 == 0 else "poin bertambah"
print ("status poin: ", poin)