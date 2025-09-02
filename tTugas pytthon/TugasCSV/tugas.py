import csv

file_path = r"C:\Users\Lenovo\OneDrive\Desktop\python\TUGAS FUNCTION\TugasCSV\keuangan.csv"

with open(file_path, 'r',) as f:
        reader = csv.reader(f)
        next(reader)  

        print("Aktivitas Harian")
        print("Tanggal | Keterangan | Kategori | Jumlah")
        
        
        print("-" * 50)
        for row in reader:
            tanggal = row[0]
            ket = row[1]
            kategori = row[2]
            jumlah = int(row[3])
            print(f"{tanggal} | {ket} | {kategori} | Rp{jumlah}")

