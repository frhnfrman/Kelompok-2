#projek python
while True:
    print("Apakah anda Pembeli atau Penjual ?")
    openp = str(input())
    if openp in ["Pembeli","pembeli"]:
        f = open("opening pembeli.txt","r")
        bacabeliopen=f.read
        print(bacabeliopen)
        f.close()
        print("tulis nomor dibawah ini untuk melakukan aksi")
        print("1.Mencari dan melihat Barang\n2.Memesan barang\n3.Keluar Aplikasi")
        aksi_beli = int(input("=>"))
        if aksi_beli == 1:
            f = open("deskripsi brng.txt","r") 
            deskrip_brng= f.read()
            print(deskrip_brng)
            Keluar1 = str(input(("Apakah Anda Ingin Kembali Ke halaman Utama?(Ya/Tidak)  ")))
            if Keluar1 in ["Ya","ya","y"]:
                pass
            else:
                break


        elif aksi_beli == 2:
            print('no')
        elif aksi_beli == 3:
            pass
        else:
            print('inputan salah,coba lagi')



    elif openp in ["Penjual","penjual"]:
        f = open("opening penjual.txt","r")
        bacajualopen=f.read()
        print(bacajualopen)
        print("tulis nomor dibawah ini untuk melakukan aksi")
        print("1.Menambah/ menjual barang\n2.info pemesan barang\n3.Keluar Aplikasi")
        aksi_jual=int(input('=>'))
        if aksi_jual == 1:
            nama_brng=str(input('masukkan nama barang'))
            harga_brng=int(input('masukkan harga yang ngotak'))
            material_brng=str(input('masukkan material barang'))
            f = open('deskripsi brng.txt','a')
            deskrip_baru="name = {} , harga = {} , material = {}".format(nama_brng,harga_brng,material_brng)
            f.write("\n") 
            f.write(deskrip_baru)
            print("Data sudah dimasukkan")
            f.close
        elif aksi_jual == 2:
            print('no')
        elif aksi_jual == 3:
            pass
        else:
            print('inputan salah,coba lagi')
    else :
        print("Input Salah,Masukkan Jawaban dengan benar")