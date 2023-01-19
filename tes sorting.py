f = open('Deskripsiread.txt', 'a')
nama_brng = str(input('Masukkan Nama Barang : '))
harga_brng = int(input('Masukkan Harga Barang : '))
material_brng = str(input('Masukkan Material Barang : '))
deskrip_read = "\nNama Barang : {}\nHarga Barang : {}\nMaterial : {}".format(nama_brng, harga_brng, material_brng)
f.write("="*60)
f.write(deskrip_read)
f.close

with open('Deskripsi.txt','a') as file:
    deskrip_baru="{},{},{},".format(nama_brng,harga_brng,material_brng)
    file.write(deskrip_baru)
    f.write('\n')
with open('deskripsi_harga_sort','a') as h:
    deskrip_baru_harga="{},{},{},".format(harga_brng,nama_brng,material_brng)
    h.write(deskrip_baru_harga)
    with open('deskripsi_harga_sort','r') as ha:
        harga=ha.readlines()
        harga.sort()
        harga1=str(harga)
        with open('deskripsi_harga_sort','a') as ha:
            ha.write(harga1)