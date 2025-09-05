import csv
# tambahkan module 'csv' dengan 'import'
print("Materi 11 - File Handling Part 2")
print("---------UPDATE CSV-----------")
# BACA isi ILE -> EKSTRAK data -> buat data baru
# -> tulis ulang semua isi barisnya dengan mode 'w'
file_path_csv = r"C:\Users\Lenovo\OneDrive\Desktop\python\MATERI-kelas\jajn.csv"
# siapkan data jajan kosong untuk menampung data dari csv ke list
data_jajan = []
# 1. Baca seluruh data
with open(file_path_csv, "r") as file_jajan:
    # csv.reaader( -> membaca isi file csv)
    isi_table_jajan = csv.reader(file_jajan)
    # ekstrak semua data dengan for loop
    for item_jajan in isi_table_jajan:
        print(item_jajan)
        # tambah item ke list data jajan
        data_jajan.append(item_jajan)

print(f"List data jajan -> {data_jajan}")

# 2. mengubah atau membbuat data baru
for item in data_jajan:
    print(f"Proses Item No => {item[0]}")
    print(item)
    #jika kolom nama adalah "x nama"
    if item[1] == "Dzaky":
        #ganti kolom uang (?index 2) dengan nilai baru
        uang_jajan_baru = 15000
        item[2] = uang_jajan_baru
        print(f"Data Ditemukan, gantui Uang nya ke {uang_jajan_baru}")
    print("----Loop End----")

# hapus data jajan di list index no 2
del data_jajan[2]
print(f"DATA JAJAN TERKINI: {data_jajan}")

# 4. Tulis Ulang dengan mode "w" -> write / menulis ulang semua baris
with open(file_path_csv, "w", newline="") as file_jajan:
    writer = csv.writer(file_jajan)
    # .writerows() -> tulis sekali banyak
    writer.writerows(data_jajan)
    print("data csv berhasil di tulis ulang")