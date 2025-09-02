import json
# tambahkan module 'csv' dengan 'import'
print("Materi 12 - File Handling")
print("---------READ JSON-----------")
file_path_json = r"C:\Users\Lenovo\OneDrive\Desktop\python\materi4\materi.json"
with open(file_path_json, "r") as file_materi:
    # json.load() -> membaca isi file json
    data_materi = json.load(file_materi)
    # keys:title": "BiodataSantri, total, status_santri, status_lulus, pelajaran
 #akses data json dengan "key" nya
    print(f"Judul berkas: {data_materi['title']}")
    print(f"Total Kelas A: {data_materi['total']}")
    print(f"Status Santri: {data_materi['status_santri']}")
    print(f"Status Kelulusan: {data_materi['status_lulus']}")
    print(f"Mata Pelajaran: {data_materi['pelajaran']}")
    # ekstra data list dengan foe loop
    for pelajaran in data_materi['pelajaran']:
        print(f"--> {pelajaran}")
#ekstrak semua data array object surah
# di python disebutjuga list of dictionary
# keys surah: no, nama, ayat, turun
print("-" * 50) # gandakan simbol dgn perkalian
print("| No | Nama Surah | Ayat | Tempat Turun |")
for surah in data_materi['surah']:
    print(f"| {surah['no']} | {surah['nama']} | {surah['ayat']} | {surah['turun']} | ")