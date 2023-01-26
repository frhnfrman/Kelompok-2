while True:
    print("Apakah anda Pembeli atau Penjual ?\nAtau Ingin keluar")
    openp = str(input())
    if openp in ["Pembeli", "Pembeli"]:
        print("="*60)
        print("\tSelamat Datang Di Toko Furniture\n\t\tSelamat Berbelanja")
        print("="*60)
        print("Tulis Nomor Dibawah Ini Untuk Melakukan Aksi")
        print("1. Melihat Tampilan Barang\n2. Mencari Barang\n3. Keluar Aplikasi")
        aksi_beli = int(input("➥  "))
        if aksi_beli == 1:
            with open("deskripsiread.txt", 'r') as f:
                baca_brng = f.read()
                print(baca_brng)

        elif aksi_beli == 2:
            print('Tulis Nomor Dari Aksi Selanjutnya')
            print('1. Melihat Harga Termurah\n2. Mencari Barang langsung (Search)')
            aksi_cari = int(input('➥  '))
            if aksi_cari == 1:
                with open('deskripsi_harga_sort', "r") as harga:
                    harga1 = harga.readlines()
                    harga1.reverse()
                    print('Berikut Data Harga Barang Dari Yang Termurah')
                    print("\nHarga, Nama Barang, Material\n")
                    for x in harga1:
                        print(f"{x}")

        elif aksi_beli == 3:
            break
        else:
            print('Inputan salah, Coba lagi')

    elif openp in ["Penjual", "Penjual"]:
        print("="*60)
        print("\tSelamat Datang Penjual terhormat")
        print("="*60)
        print("Tulis Nomor Dibawah Ini Untuk Melakukan Aksi")
        print("1. Menambah/ Menjual Barang\n2. Keluar Aplikasi")
        aksi_jual = int(input('➥  '))
        if aksi_jual == 1:
            f = open('deskripsiread.txt', 'a')
            nama_brng = str(input('Masukkan Nama Barang : '))
            harga_brng = int(input('Masukkan Harga Barang : '))
            material_brng = str(input('masukkan material Barang : '))
            deskrip_read = "\nNama Barang : {}\nHarga Barang : {}\nMaterial : {}\n".format(
                nama_brng, harga_brng, material_brng)
            f.write("="*60)
            f.write(deskrip_read)
            f.close()

            with open('deskripsi.txt', 'a') as file:
                deskrip_baru = "{},{},{},\n".format(
                    nama_brng, harga_brng, material_brng)
                file.write(deskrip_baru)
                deskrip_harga_sort = "{}, {}, {},\n".format(
                    harga_brng, nama_brng, material_brng)
                with open('deskripsi_harga_sort', 'a') as h:
                    h.write(deskrip_harga_sort)

            keluar2 = str(
                input("Apakah Anda Ingin Kembali Ke Halaman Utama ? Ya/Tidak : "))
            if keluar2 in ["Ya", "ya", "y"]:
                print('Data Akan Disimpan Setelah Keluar Aplikasi')
                continue
            else:
                print('Data Sudah Dismpan')
                break
        elif aksi_jual == 2:
            break
        else:
            print("Inputan error, Aplikasi akan ditutup")
            break
    else:
        print("Apakah Benar ? Ya/Tidak : ")
        keluarr = str(input("➥  "))
        if keluarr in ["yes"]:
            break
        else:
            continue
