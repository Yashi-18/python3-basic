print("MATERI 9 - PYTHON 3 FUNCTION")
print("-----------------------------")

# function tidak akan di eksekusi jika tidak terpanggil
def say_hello(name):
    #print("hello mr ", name)
    #kasih f di awal string untung menyisipkan variable / parameter
    #dengan diapit {nama_variabel}
    print(f"hello mr , {name}")
    print("baek baek aee")

#lambda untuk menulis fungsi yg ringkas dengan 1 baris saja
#sering disebut juga fungsi anonim (tanpa nama)

say_hello_bocil = lambda name: print(f"Hello mr.{name}")

say_hello("Evan")
say_hello("Zayn")
print("-----------------")
say_hello_bocil("Azzam")
say_hello_bocil("Ziyad")

#contoh penerapan lambda dgn higher-order function
# map() -- sorted() -- filter()
jajan_mingguan = [50000, 30000, 70000, 10000, 45000, 15000]
urutkan_uang = sorted(jajan_mingguan)
urutkan_uang_terbalik = sorted(jajan_mingguan, reverse=True)
print(f"Urutan Uang : {urutkan_uang}")
print(f"Urutan Uang Terbalik : {urutkan_uang_terbalik}")
#map() -> mentransformasi data
kurangin_uang = map(lambda uang: uang - 5000, jajan_mingguan)
list_kurangin_uang = list(kurangin_uang)
print(f"Map Uang berkurang: {list_kurangin_uang}")
# filter() -> menyaring / memfilter data
jajan_banyak = filter(lambda uang: uang > 30000, jajan_mingguan)
list_jajan_banyak = list(jajan_banyak)
print(f"Filter jajan diatas 30 rb : {list_jajan_banyak}")