print("MATERI 7 - PYTHON DATA STRUCTURE")
print("--------------------------------")

# Set -> {} -> tidak berurutan, berubah, tidak duplikat
game_azka = {"valorant", "delta", "roblox", "pointblank"}
geme_dzaky = {"minecraft", "roblox", "fnf", 'repo'}
game_azka.remove('delta')
geme_dzaky.add('roblox')

print("Game Azka :", game_azka)
print("Game Dzaky :", geme_dzaky)
game_gabungan = game_azka | geme_dzaky # | (or) atau
print("Daftar Game :", game_gabungan)

#for (loop) untuk mengeluarkan isi item dr set
for game in game_gabungan:
    print(game)
    print("---> transfer data", game , "ke PS-5")

# Dictionary (dict) -> {keyvalue} / {kuncinilai}
# -> berurutan, berubah, tdk duplikat
kamus_anime = {
    "one piece": "monkey de luffy",
    "blue lock": "isagi",
    "demon slayer": "tanjiro",
    "waifu": {
        "one piece": "big mom",
        "naruto": "tsunade",
        "demon slayer": "nezuko"
    }
}
print("Kamus anime :", kamus_anime)
print("MC demon slayer:", kamus_anime["demon slayer"])
print("Waifu one pice:", kamus_anime["waifu"]["one piece"])

# nambah item baru di dictionary
kamus_anime["overflow"] = "akane"
print("MC dr overflow:", kamus_anime ["overflow"])
#mengubah item dr dictionary
kamus_anime["demon slayer"] = "Zenitsu"
# menghapus item dr dictionary
del(kamus_anime['blue lock'])
print("Kamus Anime terbaru : ", kamus_anime)

# mengecek key / value nya
print("one piece" in kamus_anime)

# cara ngecek key ada apa aja
print(kamus_anime.keys())

# cara untuk ngecek ada value nya
print(kamus_anime.values())

#looping

for key in kamus_anime:
    print(key)

for value in kamus_anime.values():
    print(value)

for key, value in kamus_anime.items():
    print(f"(key)  -> (value)")

# nested dictionary