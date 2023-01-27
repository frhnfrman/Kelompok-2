def Read_barang():              #Fungsi Read
    with open ("deskripsi.txt",'r') as f:
        baca_brng = f.readlines()
        for a in baca_brng:
            a = a.split(',')
            print("="*60)
            print(f"{'Nama barang :'}{a[0]}")
            print(f"{'Harga Barang : '}{a[1]}")
            print(f"{'Material Barang : '}{a[2]}")
    return a

def Read_Sort():                #Fungsi Read data sorted
    with open('deskripsi_harga_sort',"r") as harga:
            harga1 = harga.readlines()
            harga1.sort()
            print('berikut data harga barang dari yang murah')
            print('-'*60)
            print(f"|{'Nama Barang':16}|{'Harga Barang':20}|{'Material':15}|")
            print('-'*60)
            for x in harga1:
                x = x.split(',')
                print(f"|{x[1]:16}|{x[0]:20}|{x[2]:15}|")
            print('-'*60)
            return x


while True:
                    #Menu utama
    print("\nApakah anda Pembeli atau Penjual ?\nAtau Ingin keluar?")
    openp = str(input("(pembeli/penjual/keluar)\n=>"))
    
                    #Menu Pembeli
    if openp in ["Pembeli","pembeli"]:  
        print("="*60)
        print("\tSelamat datang di Toko furniture\n\t\tSelamat Berbelanja")
        print("="*60)
        print("Tulis nomor dibawah ini untuk melakukan aksi")
        print("1.Melihat Tampilan Barang\n2.Mencari Barang\n3.Keluar Aplikasi")
        aksi_beli = int(input("=>"))
        
        if aksi_beli == 1:                 #Read data
            Read_barang()
            keluar1 = str(input("\nApakah Anda Ingin Kembali Ke halaman Utama?(Ya/Tidak)\n=>  "))
            if keluar1 not in ["Ya","ya","y","Y","YA"]:
                print("Anda Telah keluar Aplikasi")
                break
            else:
                continue
        
        elif aksi_beli == 2:                #Sort data
            print('Tulis nomor dari aksi selanjutnya')
            print('1.Melihat Harga Termurah\n2.Mencari Barang langsung(Search)')
            aksi_cari = int(input('=>'))
            if aksi_cari == 1:
                Read_Sort()
                keluar2 = str(input("\nApakah Anda Ingin Kembali Ke halaman Utama?(Ya/Tidak)\n=>  "))
                if keluar2 not in ["Ya","ya","y",'Y','YA']:
                    print("Anda Telah keluar Aplikasi")
                    break
                else:
                    continue


        elif aksi_beli == 3:
            break
        else:
         print('inputan salah,coba lagi')


                #Menu Penjual
    elif openp in ["Penjual","penjual"]:
        print("="*60)
        print("\tSelamat datang Penjual terhormat")
        print("="*60)
        print("tulis nomor dibawah ini untuk melakukan aksi")
        print("1.Menambah/ menjual barang\n2.Menghapus Barang tertentu\n3.Keluar Aplikasi")
        aksi_jual=int(input('=>'))
        
        
        if aksi_jual == 1:              #Menambah Data
            nama_brng=str(input('masukkan nama barang = '))
            harga_brng=int(input('masukkan harga yang ngotak = '))
            material_brng=str(input('masukkan material barang = '))

            with open('deskripsi.txt','a') as file:
                deskrip_baru="{},{},{},\n".format(nama_brng,harga_brng,material_brng)
                file.write(deskrip_baru)
                deskrip_harga_sort="{},{},{},\n".format(harga_brng,nama_brng,material_brng)
                with open('deskripsi_harga_sort','a') as h:
                    h.write(deskrip_harga_sort)
                
            keluar3 = str(input("Apakah Anda Ingin Kembali Ke halaman Utama?(Ya/Tidak)  "))
            if keluar3 in ["Ya","ya","y"]:
                print('data akan disimpan setelah keluar aplikasi')
                continue
            else:
                print('data sudah dismpan')
                break
        
        elif aksi_jual == 2:            #Menghapus data
            with open('deskripsi.txt','r') as f:
                baca_brng = f.readlines()
                print('<<<<Berikut beberapa perabotan di dalam list>>>>')
                print('-'*60)
                print(f"|{'Nama Barang':16}|{'Harga Barang':20}|{'Material':15}|")
                print('-'*60)
                for a in baca_brng:
                    a = a.split(',')
                    print(f"|{a[0]:16}|{a[1]:20}|{a[2]:15}|")
                print('-'*60)
            pilih_no=int(input('Masukkan nomor barang yang akan di hapus\n=>')) - 1
            print('Apakah anda ingin menghapus barang yang anda pilih?(ya/tidak)')
            yakin=str(input('=>'))
            if yakin not in ['ya','Ya','y','YA','Y']:
                break
            with open('deskripsi.txt','r') as f:
                y=f.readlines()
                del y[pilih_no]
                y
            with open('deskripsi.txt','w') as fi:
                for x in y:
                    x=x.split(',')
                    a=x[0]
                    b=x[1]
                    c=x[2]
                    z="{},{},{},\n".format(a,b,c)
                    fi.write(z)
            with open('deskripsi_harga_sort','r') as fii:
                yy=fii.readlines()
                del yy[pilih_no]
                yy
                with open('deskripsi_harga_sort','w') as fil:
                    for k in yy:
                        k=k.split(',')
                        aa=k[0]
                        bb=k[1]
                        cc=k[2]
                        v="{},{},{},\n".format(aa,bb,cc)
                        fil.write(v)
            print('data sudah terhapus')
            keluar4 = str(input("\nApakah Anda Ingin Kembali Ke halaman Utama?(Ya/Tidak)\n=>  "))
            if keluar4 not in ["Ya","ya","y",'Y','YA']:
                print("Anda Telah keluar Aplikasi")
                break
            else:
                continue

        elif aksi_jual == 3:
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
#Kurang Searching
