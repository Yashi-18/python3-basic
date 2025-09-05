import doa_harian
import hitung_uang
import ranking
import emoji_mood

# manggil file yg d importnya dulu, baru isinya. Kallo g ada langsung panggil isinya, dia g bakal nemu
print('Bacaan bacaan doa :')
doa_harian.doa_banguntidur()
doa_harian.doa_tidur()

print(doa_harian.doa_bersin)
print("-" * 75)

uangJajan = [50000, 30000, 15000, 70000, 10000]
print("Urutan uang jajan :")
print(hitung_uang.tambah_bonus(uangJajan))
print("-" * 75)

nilai = [75, 90, 60, 88, 100, 55]

print("Urutan ranking :")
print(ranking.urtukan_nilai(nilai))
print("-" * 75)

mood = ["senang", "biasa", "sedih", 'semangat']
print("Emoji emoji")
print(emoji_mood.convert_emoji(mood))