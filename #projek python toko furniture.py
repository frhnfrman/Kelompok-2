def Read_barang():  # Fungsi Read
    with open("deskripsi.txt", 'r') as f:
        baca_brng = f.readlines()
        for a in baca_brng:
            a = a.split(',')
            print("="*60)
            print(f"{'Nama barang : '}{a[0]}")
            print(f"{'Harga Barang : '}{a[1]}")
            print(f"{'Material Barang : '}{a[2]}")
    return a


def Read_Sort():  # Fungsi Read data sorted
    with open('deskripsi_harga_sort', "r") as harga:
        harga1 = harga.readlines()
        harga1.sort()
        print('Berikut Data Harga Barang Dari Yang Termurah')
        print('-'*60)
        print(f"|{'Nama Barang':16}|{'Harga Barang':20}|{'Material':15}|")
        print('-'*60)
        for x in harga1:
            x = x.split(',')
            print(f"|{x[1]:16}|{x[0]:20}|{x[2]:15}|")
        print('-'*60)
        return x


while True:
    # Menu utama
    print("\nApakah Anda Pembeli atau Penjual ?\nAtau Ingin keluar?")
    openp = str(input("(Pembeli/Penjual/Keluar)\n➣  "))

    # Menu Pembeli
    if openp in ["Pembeli", "pembeli"]:
        print("="*60)
        print("\tSelamat Datang Di Toko Furniture\n\t\tSelamat Berbelanja")
        print("="*60)
        print("Pilih Nomor Dibawah Ini Untuk Melakukan Aksi")
        print("1. Melihat Tampilan Barang\n2. Mencari Barang\n3. Keluar Aplikasi")
        aksi_beli = int(input("➣  "))

        if aksi_beli == 1:  # Read data
            Read_barang()
            keluar1 = str(
                input("\nApakah Anda Ingin Kembali Ke Halaman Utama ? (Ya/Tidak)\n➣  "))
            if keluar1 not in ["Ya", "ya", "y", "Y", "YA"]:
                print("Anda Telah keluar Aplikasi")
                break
            else:
                continue

        elif aksi_beli == 2:  # Sort data
            print('Pilih Nomor Dari Aksi Selanjutnya')
            print('1. Melihat Harga Termurah\n2. Mencari Barang langsung (Search)')
            aksi_cari = int(input('➣  '))
            if aksi_cari == 1:
                Read_Sort()
                keluar2 = str(
                    input("\nApakah Anda Ingin Kembali Ke Halaman Utama ? (Ya/Tidak)\n➣  "))
                if keluar2 not in ["Ya", "ya", "y", 'Y', 'YA']:
                    print("Anda Telah keluar Aplikasi")
                    break
                else:
                    continue

        elif aksi_beli == 3:
            break
        else:
            print('Inputan Salah, Coba Lagi')

            # Menu Penjual
    elif openp in ["Penjual", "penjual"]:
        print("="*60)
        print("\tSelamat Datang Penjual Terhormat")
        print("="*60)
        print("Pilih Nomor Dibawah Ini Untuk Melakukan Aksi")
        print(
            "1. Menambah/Menjual Barang\n2. Menghapus Barang Tertentu\n3. Mengganti Data Barang\n4. Keluar Aplikasi")
        aksi_jual = int(input('➣  '))

        if aksi_jual == 1:  # Menambah Data
            nama_brng = str(input('● Masukkan Nama Barang : '))
            harga_brng = int(input('● Masukkan Harga Barang : '))
            material_brng = str(input('● Masukan Material Barang : '))

            with open('deskripsi.txt', 'a') as file:
                deskrip_baru = "{},{},{},\n".format(
                    nama_brng, harga_brng, material_brng)
                file.write(deskrip_baru)
                deskrip_harga_sort = "{},{},{},\n".format(
                    harga_brng, nama_brng, material_brng)
                with open('deskripsi_harga_sort', 'a') as h:
                    h.write(deskrip_harga_sort)

            keluar3 = str(
                input("Apakah Anda Ingin Kembali Ke Halaman Utama ? (Ya/Tidak) : "))
            if keluar3 in ["Ya", "ya", "y"]:
                print('Data Akan Disimpan Setelah Keluar Aplikasi')
                continue
            else:
                print('Data Sudah Disimpan')
                break

        elif aksi_jual == 2:  # Menghapus data
            with open('deskripsi.txt', 'r') as f:
                baca_brng = f.readlines()
                print('⤥ Berikut Beberapa Perabotan Di Dalam List ⤦')
                print('-'*60)
                print(f"|{'Nama Barang':16}|{'Harga Barang':20}|{'Material':15}|")
                print('-'*60)
                for a in baca_brng:
                    a = a.split(',')
                    print(f"|{a[0]:16}|{a[1]:20}|{a[2]:15}|")
                print('-'*60)
            pilih_no = int(
                input('Masukkan Nomor Barang Yang Akan Di Hapus\n➣  ')) - 1
            print('Apakah Anda Ingin Menghapus Barang Yang Anda Pilih ? (Ya/Tidak) ')
            yakin = str(input('➣  '))
            if yakin not in ['ya', 'Ya', 'y', 'YA', 'Y']:
                break
            with open('deskripsi.txt', 'r') as f:
                y = f.readlines()
                del y[pilih_no]
            with open('deskripsi.txt', 'w') as fi:
                for x in y:
                    x = x.split(',')
                    a = x[0]
                    b = x[1]
                    c = x[2]
                    z = "{},{},{},\n".format(a, b, c)
                    fi.write(z)
            with open('deskripsi_harga_sort', 'r') as fii:
                yy = fii.readlines()
                del yy[pilih_no]
                with open('deskripsi_harga_sort', 'w') as fil:
                    for k in yy:
                        k = k.split(',')
                        aa = k[0]
                        bb = k[1]
                        cc = k[2]
                        v = "{},{},{},\n".format(aa, bb, cc)
                        fil.write(v)
            print('Data Sudah Terhapus')
            keluar4 = str(
                input("\nApakah Anda Ingin Kembali Ke Halaman Utama ? (Ya/Tidak)\n➣  "))
            if keluar4 not in ["Ya", "ya", "y", 'Y', 'YA']:
                print("Anda Telah keluar Aplikasi")
                break
            else:
                continue

        elif aksi_jual == 3:  # Mengganti data barang
            with open('deskripsi.txt', 'r') as f:
                baca_brng = f.readlines()
                print('⤥ Berikut Beberapa Perabotan Di Dalam List ⤦')
                print('-'*60)
                print(f"|{'Nama Barang':16}|{'Harga Barang':20}|{'Material':15}|")
                print('-'*60)
                for a in baca_brng:
                    a = a.split(',')
                    print(f"|{a[0]:16}|{a[1]:20}|{a[2]:15}|")
                print('-'*60)
            pilih_no = int(
                input('Masukkan Nomor Barang Yang Akan Di diganti\n➣  ')) - 1
            print('Apakah Anda Ingin Mengganti Barang Yang Anda Pilih ? (Ya/Tidak) ')
            yakin = str(input('➣  '))
            if yakin not in ['ya', 'Ya', 'y', 'YA', 'Y']:
                break
            namabarang = str(input('● Masukkan Nama Barang baru : '))
            hargabarang = int(input('● Masukkan Harga barang baru : '))
            materilbarang = str(input('● Masukkan Material barang baru : '))
            barangganti = "{},{},{},".format(
                namabarang, hargabarang, materilbarang)
            barangganti2 = "{},{},{},".format(
                hargabarang, namabarang, materilbarang)
            with open('deskripsi.txt', 'r') as f:
                y = f.readlines()
                del y[pilih_no]
                y.insert(pilih_no, barangganti)
            with open('deskripsi.txt', 'w') as fi:
                for x in y:
                    x = x.split(',')
                    a = x[0]
                    b = x[1]
                    c = x[2]
                    z = "{},{},{},\n".format(a, b, c)
                    fi.write(z)
            with open('deskripsi_harga_sort', 'r') as fii:
                yy = fii.readlines()
                del yy[pilih_no]
                yy.insert(pilih_no, barangganti2)
                with open('deskripsi_harga_sort', 'w') as fil:
                    for k in yy:
                        k = k.split(',')
                        aa = k[0]
                        bb = k[1]
                        cc = k[2]
                        v = "{},{},{},\n".format(aa, bb, cc)
                        fil.write(v)
            print('Data Sudah Terganti')
            keluar4 = str(
                input("\nApakah Anda Ingin Kembali Ke Halaman Utama ? (Ya/Tidak)\n➣  "))
            if keluar4 not in ["Ya", "ya", "y", 'Y', 'YA']:
                print("Anda Telah keluar Aplikasi")
                break
            else:
                continue

        elif aksi_jual == 4:
            break

        else:
            print("Inputan Error, Aplikasi Akan Ditutup")
            break
    else:
        print("Apakah Benar ? (Ya/Tidak)")
        keluarr = str(input("➣  "))
        if keluarr in ["Ya"]:
            break
        else:
            continue
# Kurang Searching,Deleting
