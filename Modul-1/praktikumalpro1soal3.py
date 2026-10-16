#diketahui
#jarak 100km
#konsumsi bahan bakar sebesar 40km untuk setiap 1 liter 
#sebelum berangkat ada sisa bensin sebesar 1,5l 
#harga bensin per liter adalah 10.000

#ditanyakan
#jarak tempuh
jarak = 100
jarak_pp = (jarak * 2)
print ("total jarak yang harus ditempuh oleh dimas untuk pulang dan pergi adalah", jarak_pp)

#total bensin yang dibutuhkan
jarakPerliter = 40
total_bensin_dibutuhkan = (jarak_pp / jarakPerliter)
print ("jadi bensin yang dibutuhkan untuk perjalanan pulang dan pergi adalah", total_bensin_dibutuhkan)

#total bensin yang harus dibeli
sisaBensin = 1.5
bensin_harus_dibeli = (total_bensin_dibutuhkan - sisaBensin)
print ("jumlah bahan bakar yang harus dibeli oleh dimas adalah", bensin_harus_dibeli)

#total biaya untuk membeli bensin 
hargaBensin = 10.000
totalBiaya = (hargaBensin * bensin_harus_dibeli)
print ("total biaya yang harus dimas keluarkan untuk membeli bensin adalah sebesar", totalBiaya)

