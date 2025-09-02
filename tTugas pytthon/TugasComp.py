from datetime import date

tahun_sekarang = date.today().year

nama = input("Siapa nama mu?")
umur = int(input("Umur lu sekarang dh berapa?"))
kelas = input("Sekarang lu kls brp?")
cita_Cita = input("Nanti pas gede lu mau jd apa?")
hobi = input("Hobi favorit lu apa?")
waktu = input("Kalo belajar lebih suka 'pagi' atau 'malam' ?")

print("====As-Suaalus Saanii..====")

print("Masukkan tipe pilihan kesukaan lu disini..")
print("1. Wibu")
print("2. Gamer")
print("3. K-Popers")
print("4. Anak Konten")
print("5. Anak Nongki")


pilihan_digital = input("Masukan pilihan kamu")

if pilihan_digital == "wibu":
    waifu = input("masukan nama waifu mu : ")
    print("Cih...g selevel ama gua bro")

elif pilihan_digital == "gamer":
    game = input("Game apa yg lu mainin?")
    print("Kapan kapan mabar lah..")

elif pilihan_digital == "kpop":
    bias = input("siapa bias kamu?")
    print("umm..sorry gtau :/")

elif pilihan_digital == "ngonten":
    konten = input("Lu klo ngonten dimana?(platformnya)")
    print("Gw follow tuh akun nanti :D")

elif pilihan_digital == "nongki":
    tongkrongan = input("Nongkrong paling sering dimana?")
    print("Klo gw sih rekomenin ke Summarecon sih")

else:
    print("Sok asik bet sih lu, ditanya apa jawab apa")

print("---Babak bonus---")

bonus =input("Apakah tmn sebelah mu bau? (y/g)")

if bonus == "y":
    print("Cooba bilang ke dia: 'Maneh geus ibak can?'")

elif bonus == ("g"):
    print("Ooh...Y udah sih, cmn nanya doang")

else:
    print("lu tuh g di ajak pea..")

tahun_lahir = tahun_sekarang - umur
print("<--------------------->")
print("Ini data yg udh lu masukin:")
print("Nama lu :", nama)
print("Umur lu :", umur)
print("Sekarang kelas :", kelas)
print("cita cita lu jadi:", cita_Cita)
print("Hobi lu :", hobi)
print("Lu lebih suka belajar", waktu)
print("Tahun lahir :", tahun_lahir)

print("<=========================>")
print(" Tipe yg dh lu pilih td ===>>>")
print("Tipe lu:", pilihan_digital)
print("Jgn lupa ttp ibadah y...")

print("<--------------------->")
print("<<<FAKTA SEBENARNYA>>>")
print("Temen yg td lu maksud bau kgk? ", bonus)
print("🚨🚨🚨 Aib seseorg terbongkar🚨🚨🚨")