print("MATERI 8 - FUNCTION BASIC")
print("--------------------------------")
# functiom di awali dengan keyword 'def'
def halo_ngab():
    print("Halo ngab")
    print("Halo jg ngab")
# function dengan parameter 'nama'
def sapa_sapa(nama):
    print("Halo bang ", nama)
    print("Apa kabar bang", nama)
    print("---------------")

print("Cobain fungsinya:")
halo_ngab()
sapa_sapa("Dzaky")
sapa_sapa("Ziyad")

# funsi luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    print(">Panjang:", panjang)
    print(">Lebar:", lebar)
    rumus = panjang * lebar
    print("Luas persegi panjang =", rumus)

luas_persegi_panjang(10, 20)
luas_persegi_panjang(50, 20)