#projek python
while True:
    print("Apakah anda Pembeli atau Penjual ?")
    openp = str(input())
    if openp in ["Pembeli","pembeli"]:  
        print("="*60)
        print("\tSelamat datang di Toko furniture\n\t\tSelamat Berbelanja")
        print("="*60)
        print("Tulis nomor dibawah ini untuk melakukan aksi")
        print("1.Melihat Tampilan Barang\n2.Mencari Barang\n3.Keluar Aplikasi")
        aksi_beli = int(input("=>"))
        if aksi_beli == 1:
            with open ("deskripsi brng.txt",'r') as f:
                baca_brng = f.readlines()
                list_brng = [baca_brng[0],baca_brng[1],baca_brng[2]]
                for a in baca_brng:
                    print(f"Nama Perabotan\t: {list_brng[0]}")
                    print(f"Harga Perabotan\t: {list_brng[1]}")
                    print(f"Material\t: {list_brng[2]}")
                    print("-"* 60)

        #elif aksi_beli == 2:
            

        elif aksi_beli == 3:
            break
        else:
         print('inputan salah,coba lagi')



    elif openp in ["Penjual","penjual"]:
        print("="*60)
        print("\tSelamat datang Penjual terhormat")
        print("="*60)
        print("tulis nomor dibawah ini untuk melakukan aksi")
        print("1.Menambah/ menjual barang\n2.Keluar Aplikasi")
        aksi_jual=int(input('=>'))
        if aksi_jual == 1:
            nama_brng=str(input('masukkan nama barang = '))
            harga_brng=int(input('masukkan harga yang ngotak = '))
            material_brng=str(input('masukkan material barang = '))
            deskrip_baru="{}${}${}".format(nama_brng,harga_brng,material_brng)
            f = open('deskripsi brng.txt','a')
            f.write("\n")
            f.write(deskrip_baru)
            print("Data tersimpan")
            f.close
            keluar2 = str(input("Apakah Anda Ingin Kembali Ke halaman Utama?(Ya/Tidak)  "))
            if keluar2 in ["Ya","ya","y"]:
                print('data akan disimpan setelah keluar aplikasi')
                continue
            else:
                print('data sudah dismpan')
                break
        elif aksi_jual == 2:
            print('no')
        elif aksi_jual == 3:
            pass
        else:
            print('inputan salah,coba lagi')
    else :
        print("Input Salah,Masukkan Jawaban dengan benar")
