import csv

# baca semua data dari csv
with open("masalahKeuangan.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)

print("\n")

# 1. tampilkan semua data
print("📌 Semua Data : ")
for baris in data:
    print(f"{baris['Tanggal']} |{baris['Keterangan']} |{baris['Kategori']} |{baris['Jumlah']} ")
    
# 2. hitung semua pengeluaran    \\\\sum cuma nerima angka
total = sum(int(baris['Jumlah']) for baris in data)
print(f" TOTAL PENGELUARAN: Rp{total}")

# 3. menghitung Total perkategori
kategori_total = {}
for baris in data:
    kategori = baris['Kategori']
    jumlah = int(baris['Jumlah'])
    if kategori not in kategori_total:
        kategori_total[kategori] = 0
    kategori_total[kategori] += jumlah

print("📊 pengeluaran per kategori : ")
for kategori, jumlah in kategori_total.items():
    print(f"- {kategori} : Rp.{jumlah}")

# 4. kategori terbesar


