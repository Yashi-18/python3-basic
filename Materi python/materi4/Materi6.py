# Python data structure

# list [] (berurutan, bisa d ubah, boleh duplikat)
daftar_belanja = [
    "Teh desa", # index 0
    "Naspad", # index 1
    "Gorengan" # index 2
    ]

# [no index] mengakses list lewat index
print("isi tas belanja :", daftar_belanja)
print("item ke-1:", daftar_belanja[0])
print("item ke-2", daftar_belanja[2])

#append() menambah item baru ke akhir list
daftar_belanja.append("olive chicken")
daftar_belanja.append("gabin")
print("isi tas belanja skrg:", daftar_belanja)
print("item ke-4", daftar_belanja[3])

#insert() menambah item baru ke index yg mau kita pilih di list
daftar_belanja.insert(2, "lokita")
print(daftar_belanja)

#remove() menghapus item dr list
daftar_belanja.remove("Gorengan")
print("isi tas belanja akhir:", daftar_belanja)

print("-------TUPLE-------")
# tuple (berurut, tdk bisa d ubah, boleh duplikat)
# penulisannya menggunakan ()
ttl = ("Bandung", 1, "Juli", 1998)
print("tgl lahir ujang :", ttl)

#[no_index] akses data tuple
print("tempatL", ttl[0])
print("Tanggal:", ttl[1])
print("Bulan:", ttl[2])
print("Tahun:", ttl[3])
# akses bulan (posisi index nya) : lalu batas akhir item nya
print("Bulan tahun:", ttl[3:4])

# Unpacking tuple ke variable baru
#mengikuti urtan itemmnya
tempat_lahir, tgl_lahir, bulan_lahir, thn_lahir = ttl
print(tempat_lahir)

#manipulasi list lanjutan
jajan_ujang = ["pentol", "cireng"]
jajan_asep = ["bakso", "nasgor"]
jajan_ujang_dan_asep = jajan_ujang + jajan_asep
print(jajan_ujang_dan_asep)
# list multi-dimensi
list_minuman = [
    ["kopi", "susu", "teh"], # baris 0
    ["jus apel", "jus melon", "jus jeruk"], # baeis 1
    ["es teler", "es campur", "es doger"] # baris 2
    ]
print(list_minuman)
print(list_minuman[2])
# tiap baris punya 3 index (0, 1, 2)
print(list_minuman[2][2]) # akses es doger

#tamabahan dr mas hamka
buah = ['apel','mangga','ceri','durian']
print(buah[2])
# ngubah nilainya
buah[1] = 'pisang'
print(buah)

#ngapus berdasarkan index
buah.pop(0)
print(buah)

#panjang list
print(len(buah))

# mencetak seluruh isi list menggunakan string

for item in buah:
    print(item)