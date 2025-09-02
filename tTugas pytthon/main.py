import doa_harian
import hitung_uang
# manggil file yg d importnya dulu, baru isinya. Kallo g ada langsung panggil isinya, dia g bakal nemu
doa_harian.doa_banguntidur()
doa_harian.doa_tidur()

print(doa_harian.doa_bersin)

uangJajan = [50000, 30000, 15000, 70000, 10000]
print(hitung_uang.tambah_bonus(uangJajan))