import csv

print("Materi 10 - File Handling")
print("-------------------------")
# buka file
file_path = r"C:\Users\Lenovo\OneDrive\Desktop\python\MATERI-kelas\pesan.txt"
file_pesan = open(file_path, "r")
# baca isi file 
isi_pesan = file_pesan.read()
# tampilkan output isi pesan
print(f"Isi Pesan => {isi_pesan}")
# tutup file
file_pesan.close()

print('-----OPEN CSV FILE-----')
file_path_csv = r"C:\Users\Lenovo\OneDrive\Desktop\python\MATERI-kelas\jajn.csv"
file_jajan = open(file_path_csv, "r")
isi_table_jajan = file_jajan.read()
print(f"Table Jajan => {isi_table_jajan}")
file_jajan.close()

print("----Append CSV File----")
jajan_baru = [5,"Ridho",100000]
print(f"jajan_baru: {jajan_baru}")
# open() -> membuka file dari file path
# mode 'a' -> append (tambah data)
# new line -> tambahbaris baru dengan teks kosong
# with ... as -> buka file dgn tutup otomatis
with open(file_path_csv, "a", newline="") as file_jajan:
# aktifkan mode writer csv dari file target
    writer = csv.writer(file_jajan)
# Tambahkan baris dari variable jajan baru
    writer.writerow(jajan_baru)
