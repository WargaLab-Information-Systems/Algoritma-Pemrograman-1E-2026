def evaluasi_kelayakan(pc_nama, pc_status, pc_ram_input):
    #Memeriksa apakah input RAM berupa angka yang valid
    if pc_ram_input.isdigit():
        ram_val = int(pc_ram_input)
        
        #Validasi status dan besar RAM
        if pc_status.strip().capitalize() == "Normal" and ram_val >= 8:
            kelayakan = "Layak"
        else:
            kelayakan = "Tidak Layak"
    else:
        #Jika mengandung huruf atau karakter non-angka (seperti 'Delapan')
        kelayakan = "Format RAM Kacau"
        
    #Format cetak murni menggunakan manipulasi string sesuai permintaan soal
    hasil_cetak = f'["PC": "{pc_nama}", "Status": "{kelayakan}"]'
    return hasil_cetak

def main():
    print("=== SISTEM PENDATAAN INVENTARIS PC LABORATORIUM ===")
    data_pc = []
    
    while True:
        nama = input("Masukkan Nama PC (atau ketik 'selesai' untuk berhenti): ")
        if nama.strip().lower() == 'selesai':
            break
            
        status = input(f"Masukkan Status PC {nama} (Normal/Rusak): ")
        ram = input(f"Masukkan Kapasitas RAM (GB) PC {nama}: ")
        
        #Memasukkan data ke dalam Multidimensional List
        data_pc.append([nama, status, ram])
        print("--- Data berhasil ditambahkan ---\n")

    print("\n" + "="*40)
    print("HASIL EVALUASI KELAYAKAN INVENTARIS PC:")
    print("="*40)
    
    #Mengevaluasi dan mencetak seluruh data PC
    for pc in data_pc:
        nama_pc = pc[0]
        status_pc = pc[1]
        ram_pc = pc[2]        
        #Memanggil fungsi kustom evaluasi
        output_string = evaluasi_kelayakan(nama_pc, status_pc, ram_pc)
        print(output_string)

main()