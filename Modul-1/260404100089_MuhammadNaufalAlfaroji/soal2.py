import math
#rumus volume kerucut : V = 1/3 * π * r**2 * t  atau
#  (1/3) * 3.14 * (jari_jari ** 2) * tinggi
 

jari_jari = float(input("masukkan jari jari alas:",))
tinggi_kerucut = float(input("masukkan tinggi kerucut:",))

volume = (1/3) * 3.14 * (jari_jari ** 2) * tinggi_kerucut

print("volume kerucut =", volume)