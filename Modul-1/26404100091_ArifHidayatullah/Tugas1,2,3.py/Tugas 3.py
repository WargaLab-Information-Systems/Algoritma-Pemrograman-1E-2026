#Menentukan variabel secara statis berdasarkan data soal 
jarak_satu_arah = 100
konsumsi_BBM = 40 
sisa_bensin = 1.5
harga_perliter = 10000

total_jarak = jarak_satu_arah * 2
total_kebutuhan_BBM = total_jarak / konsumsi_BBM
BBM_yang_harus_dibeli = total_kebutuhan_BBM - sisa_bensin
total_biaya = BBM_yang_harus_dibeli * harga_perliter

print("=== Hasil perhitungan perjalanan pulang-pergi dimas ===")
print(f"a. total jarak perjalanan pulang pergi : {total_jarak} km")
print(f"b. total kebutuhan bahan bakar : {total_kebutuhan_BBM} liter")
print(f"c. bahan bakar yang harus dibeli : {BBM_yang_harus_dibeli} liter")
print(f"d. total biaya yang harus dikeluarkan : {total_biaya} ")