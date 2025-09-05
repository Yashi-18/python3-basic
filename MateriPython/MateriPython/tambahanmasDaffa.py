import csv

file_path = r"C:\Users\Lenovo\OneDrive\Desktop\python\MATERI-kelas\jajn.csv"

with open(file_path, "r") as  file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read = list(read)

    print("SEMUA DATA")
    print("-" * 50)

    for baris in list_read:
        nomor = baris[0]
        nama = baris[1]
        uang = baris[2]

        print(f"{nomor} | {nama} | {uang}")

#Tambah data
with open(file_path, 'a', newline="") as file_baru:
    write = csv.writer(file_baru)
    write.writerow(["5", "Wildan", "20000"])