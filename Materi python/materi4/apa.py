
x = 10 * 10
y = 20 / 5
print(x, y)

# operator += (y = y + 5)
y += 20

# input() berguna menerima inputan dr user
nilaiUmur = input("berapa umur lu?")
print("Umur lu", nilaiUmur, "tahun")
#if - else statement
#if - (jika terpenuhi) - else (selainnya atau tdk terpenuhi)
# operator pembnading == != > <
if (nilaiUmur == 25):
    print("Umur nya ketuaan")
elif (nilaiUmur == 10):
    print("Umur lu kemudaan cil")
else:
    print("umurnya cukup")

# operator != (tidak sam dengan)
kelasBudi = "A"
statusKelasBudi = kelasBudi != "C" #True
print("statusKelasBudi: ", statusKelasBudi)

statusKehadiran = "hadir"
if (statusKehadiran != "alpa"): #tidak sama dgn alpa
    print("mendapatkan point +1")
else: #statusnya alpa
  print("mendapatkan poin -1")
