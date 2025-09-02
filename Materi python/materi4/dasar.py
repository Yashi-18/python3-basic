print("Python ganteng")
# for loop (index di muali dr 0 - 5)
for angka in range(0, 5):
    print("Halo ke-", angka)
    print("mantap!") 
    print("---selesai---")# ini gk akan masuk loop karna diluar blok kode
#for loop ke string
sandiWifi = "hsijoglo"
for huruf in sandiWifi:
    print(huruf, "==>")
    #white loop (ulangi sampai kondisi terpenuhi)
    no = 1
    batas = 10
    while (no < batas):
        #print("ulangi ke-", no)
        print("*" * no)
        no += 1

        #kalau looping trs berjalan, tekan Ctrl + C
        #untukmembatalkan eksekusi program

        # simulasi flowchart buat sim
        print("---mulai---")
        cekUmur = input("Berapa umur anda?")
        #konversi / mengganti tipe data suATU variabel
        #fungsi int() mengganti string ke interger
        angkaUmur = int(cekUmur)
        if (angkaUmur >= 18):
            print("Boleh buat sim baru")
        else:
            print("Masih bocil dek...")

            print('--Selesai--')