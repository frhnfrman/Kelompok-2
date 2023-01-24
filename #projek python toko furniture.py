while True:
    print("Apakah anda Pembeli atau Penjual ?\nAtau Ingin keluar")
    openp = str(input())
    if openp in ["Pembeli","pembeli"]:  
        print("="*60)
        print("\tSelamat datang di Toko furniture\n\t\tSelamat Berbelanja")
        print("="*60)
        print("Tulis nomor dibawah ini untuk melakukan aksi")
        print("1.Melihat Tampilan Barang\n2.Mencari Barang\n3.Keluar Aplikasi")
        aksi_beli = int(input("=>"))
        if aksi_beli == 1:
            with open ("deskripsiread.txt",'r') as f:
                baca_brng=f.read()
                print(baca_brng)

        elif aksi_beli == 2:
            print('Tulis nomor dari aksi selanjutnya')
            print('1.Melihat Harga Termurah\n2.Mencari Barang langsung(Search)')
            aksi_cari = int(input('=>'))
            if aksi_cari == 1:
                with open('deskripsi_harga_sort',"r") as harga:
                    harga1 = harga.readlines()
                    harga1.reverse()
                    print('berkut data harga barang dari yang murah')
                    print("\nHarga,Nama Barang,Material\n")
                    for x in harga1:
                        print(f"{x}")



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
            f = open('deskripsiread.txt','a')
            nama_brng=str(input('masukkan nama barang = '))
            harga_brng=int(input('masukkan harga yang ngotak = '))
            material_brng=str(input('masukkan material barang = '))
            deskrip_read="\nNama Barang : {}\nHarga Barang : {}\nMaterial :{}\n".format(nama_brng,harga_brng,material_brng)
            f.write("="*60)
            f.write(deskrip_read)
            f.close()

            with open('deskripsi.txt','a') as file:
                deskrip_baru="{},{},{},\n".format(nama_brng,harga_brng,material_brng)
                file.write(deskrip_baru)
                deskrip_harga_sort="{},{},{},\n".format(harga_brng,nama_brng,material_brng)
                with open('deskripsi_harga_sort','a') as h:
                    h.write(deskrip_harga_sort)
                
            keluar2 = str(input("Apakah Anda Ingin Kembali Ke halaman Utama?(Ya/Tidak)  "))
            if keluar2 in ["Ya","ya","y"]:
                print('data akan disimpan setelah keluar aplikasi')
                continue
            else:
                print('data sudah dismpan')
                break
        elif aksi_jual == 2:
            break
        else:
            print("inputan Error,Aplikasi akan ditutup")
            break
    else :
        print("Apakah benar?(yes/no)")
        keluarr = str(input("=>"))
        if keluarr in ["yes"]:
            break
        else:
            continue
