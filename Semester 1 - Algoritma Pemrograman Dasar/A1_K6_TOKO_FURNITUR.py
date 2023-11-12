# Algoritma Pemrograman Dasar Semester 1
# Made by Muhammad Arya Fayyadh Razan, Ammar Nabil Fauzan, and Oktaria Indi Cahyani

# IMPORT LIBRARY
import os                           # Untuk mengecek sistem operasi
from tabulate import tabulate       # Untuk membuat tabel
from datetime import datetime       # Untuk menampilkan tanggal
import time                         # Untuk delay pada program

# FUNGSI UNTUK SHORTCUT
def clears():                       # Fungsi untuk membersihkan program
    sistem_operasi = os.name        # Membuat variabel baru untuk nama sistem operasi dan mengecek sistem operasi
    if sistem_operasi == "nt":      # Jika sistem operasi adalah Windows, membersihkan program
        os.system("cls")            
    else:                           # Jika sistem operasi selain Windows, membersihkan program
        os.system("clear")          

def lanjutan():                                         # Fungsi untuk lanjut ke menu berikutnya
    lanjut = input("Tekan ENTER untuk lanjut > ")       # Input untuk lanjut
    if lanjut == "":                                    # Jika inputnya ENTER atau kosong, membersihkan program
        clears()
    else:                                               # Jika inputnya selain ENTER atau kosong, membersihkan program
        clears()

# FORMAT WARNA
redc = "\033[0;31m"     # Format warna untuk warna merah
whitec = "\033[0m"      # Format warna untuk warna putih
greenc = "\033[0;32m"   # Format warna untuk warna hijau

# DATABASE
data_admin = ("haia", "haia")                                               # Tuple Data username dan password admin
data_member = {}                                                            # Dictionary Data username dan password untuk member
barang = [                                                                  # List Data barang berisi dictionary barang yang dijual
    {"KODE": 10, "NAMA": "Kursi", "HARGA": 35000, "STOK": 20},
    {"KODE": 11, "NAMA": "Kursi gimang", "HARGA": 90000, "STOK": 10},
    {"KODE": 12, "NAMA": "Kursi goyang", "HARGA": 90000, "STOK": 15}
]
keranjang = []                                                              # List data penyimpanan untuk menyimpan data keranjang
harga_dikeranjang = {}                                                      # Dictionary data penyimpanan untuk menyimpan harga harga di keranjang untuk ditotal
admin = False                                                               # Variable untuk mengecek apakah user adalah admin, default false
usernamelog = []                                                            # List data penyimpanan untuk menyimpan username yang login
riwayat_pembelian =[]                                                       # List data penyimpanan untuk menyimpan riwayat pembelian

# FUNGSI UNTUK MENU AKUN
def register():                                                                                     # Fungsi untuk membuat akun/register akun
    print("\n=======| REGISTER AKUN |=======")
    while True:                                                                                     # Perulangan sampai perulangan diberhentikan
        username = str(input("Username: "))                                                         # Input username
        username = username.lower()                                                                 # Menjadikan inputan username menjadi huruf kecil
        if len(username) < 4:                                                                       # Jika username kurang dari 4 karakter, ulangi input
            print(redc, "(!) Username minimal 4 karakter", whitec)
        elif username in data_member or username in data_admin:                                                               # Jika username sudah terdaftar, ulangi input
            print(f"{username} sudah terdaftar, cari nama lain.")
        else:                                                                                       # Jika username belum terdaftar, lanjut input password
            password = str(input("Password: "))
            if len(password) < 4:                                                                   # Jika password kurang dari 4 karakter, ulangi input
                print(redc, "(!) Password minimal 4 karakter", whitec)
            else:                                                                                   # Jika password tidak kurang dari 4 karakter, lanjut
                lanjut = input("Tekan ENTER untuk simpan dan ketik (N/NO) untuk tidak simpan > ")   # Input untuk lanjut
                if lanjut == "":                                                                    # Jika inputan ENTER atau kosong, simpan data registrasi 
                    data_member[username] = password                                                # Menyimpan username sebagai key dan password sebagai value di data_member 
                    print(greenc, "Registrasi berhasil.", whitec)
                    break                                                                           # Berhentikan perulangan
                else:                                                                               # Jika inputan selain ENTER atau kosong, gagal menyimpan
                    print(redc, "(!) Registrasi gagal.", whitec)
                    break                                                                           # Berhentikan perulangan

def login():                                                                                        # Fungsi untuk login
    print("\n========| LOGIN AKUN |========")
    global admin                                                                                    # Membuat variabel admin yang ada di fungsi ini menjadi variabel global
    coba = 0                                                                                        # Inisialisasi variabel coba
    max_coba = 3                                                                                    # Inisialisasi variabel maksimal percobaan

    while coba < max_coba:                                                                          # Perulangan untuk login, jika coba kurang dari max_coba maka masuk ke perulangan         
        username = str(input("Username: "))
        password = str(input("Password: "))

        if (username, password) == data_admin:                                                      # Jika login admin berhasil
            print(greenc, "Selamat datang, Admin!", whitec)
            admin = True                                                                            # Mengubah variabel admin menjadi True
            return admin                                                                            # Kembalikan variabel admin

        elif username in data_member and data_member[username] == password:                         # Jika login member berhasil
            print(greenc, f"Selamat datang, {username}!", whitec)
            usernamelog.clear()                                                                     # Mengosongkan list usernamelog
            usernamelog.append(username)                                                            # Menambahkan username ke list usernamelog
            admin = False                                                                           # Mengubah variabel admin menjadi False
            return admin                                                                            # Kembalikan variabel admin

        coba += 1                                                                                   # Mengupdate variabel coba dengan menambah 1
        sisa_coba = max_coba - coba                                                                 # Menghitung sisa percobaan
        print(redc, f"(!) Username atau password salah. Sisa percobaan : {sisa_coba}", whitec)

    print(redc, "(!) Anda telah melebihi batas maksimal percobaan login.", whitec)
    print("Program dihentikan.")
    exit()                                                                                          # Keluar dari program jika tidak masuk dalam perulangan

# FUNGSI UNTUK MENU MEMBER
def tampilkan_katalog():                                                                            # Fungsi untuk tampilkan katalog
    print("\nKatalog Barang :")
    format_align = ["center", "center", "center", "center"] 
    barang_copy = [item.copy() for item in barang]                                                  # Menduplikat barang menjadi barang_copy untuk diformat
    for item in barang_copy:                                                                        # Perulangan untuk format harga
        item['HARGA'] = f"RP. {item['HARGA']:,.0f}"                                                 # Mengubah format angka menjadi format rupiah
    print(tabulate(barang_copy, headers="keys", tablefmt="fancy_grid", colalign=format_align))

def isi_keranjang():
    print("\n====================| Isi Keranjang |===================")
    while True:                                                                                                                                      # Perulangan sampai perulangan diberhentikan
        tampilkan_katalog()
        pilihan_anda = input("\nSilakan pilih barang (kode barang) atau tekan ENTER untuk kembali: ")
        if pilihan_anda == "":                                                                                                                       # Jika inputan ENTER atau kosong, membersihkan program
            clears()                                                                                                                              
            break                                                                                                                                    # Berhentikan perulangan
        else:
            try:
                kode = int(pilihan_anda)
                item = next((barang_item for barang_item in barang if barang_item['KODE'] == kode), None)                                            # Mencari barang di variabel barang berdasarkan kode 
                if item is not None:                                                                                                                 # Jika barang ditemukan maka melanjutkan program
                    jumlah_barang = int(input("Jumlah barang : "))
                    if item['STOK'] >= jumlah_barang and jumlah_barang > 0:                                                                          # Jika stok mencukupi dan jumlah inputan barang lebih dari 0 maka lanjutkan program
                        keranjang_member = [barang_item for barang_item in keranjang if barang_item.get('USERNAME', '') == usernamelog[0]]           # Mengambil data keranjang berdasarkan username (keranjang member)
                        barang_ada = next((barang_item for barang_item in keranjang_member if barang_item['KODE'] == kode), None)                    # Mencari barang di variabel keranjang member berdasarkan kode
                        if barang_ada is not None:                                                                                                   # Jika barang di keranjang member ditemukan
                            if jumlah_barang == 1:                                                                                                   # Jika jumlah inputan barang sama dengan 1
                                barang_ada['JUMLAH'] += jumlah_barang                                                                                # Menambahkan jumlah barang ke keranjang member
                                barang_ada['HARGA'] += item['HARGA']                                                                                 # Menambahkan harga barang ke keranjang member
                            else:
                                barang_ada['JUMLAH'] += jumlah_barang                                                                                # Selain jumlah inputan barang sama dengan 1
                                barang_ada['HARGA'] += item['HARGA'] * jumlah_barang                                                                 # Menghitung dan menambahkan harga barang ke keranjang member
                            item['STOK'] -= jumlah_barang                                                                                            # Mengurangi stok barang                                  
                            print(greenc, f"{item['NAMA']} telah dimasukkan ke dalam keranjang.", whitec)
                        else:                                                                                                                        # Jika barang tidak ditemukan
                            harga_barang = item['HARGA'] * jumlah_barang                                                                             # Menghitung dan menambahkan harga barang                                                                         
                            baru = {"USERNAME": usernamelog[0], "KODE": kode, "NAMA": item['NAMA'], "HARGA": harga_barang, "JUMLAH": jumlah_barang}  # Membuat data keranjang baru
                            keranjang.append(baru)                                                                                                   # Menyimpan data baru ke keranjang
                            harga_dikeranjang[kode] = harga_barang                                                                                   # Menyimpan harga barang ke variabel harga di keranjang
                            item['STOK'] -= jumlah_barang                                                                                            # Mengurangi stok
                            print(greenc, f"{item['NAMA']} telah dimasukkan ke dalam keranjang.", whitec)
                    elif jumlah_barang == 0:                                                                                                         # Jika jumlah inputan barang sama dengan 0, kembali ke perulangan
                        print(redc, "(!) Jumlah barang tidak boleh 0.", whitec)
                    else:                                                                                                                            # Jika stok tidak mencukupi, kembali ke perulangan
                        print(redc, "(!) Jumlah barang melebihi stok yang tersedia.", whitec)
                else:                                                                                                                                # Jika barang tidak ditemukan, kembali ke perulangan
                    print(redc, "(!) Kode barang tidak valid.", whitec)
            except ValueError:                                                                                                                       # Jika inputan bukan angka, kembali ke perulangan
                print(redc, "(!) Inputan tidak valid.", whitec)

def cek_keranjang():                                                                                                    # Fungsi untuk cek keranjang
    print("\n====================| Cek Keranjang |===================")
    keranjang_member = [barang for barang in keranjang if barang.get('USERNAME', '') == usernamelog[0]]                 # Mengambil data keranjang berdasarkan username (keranjang member)
    if keranjang_member:                                                                                                # Jika data keranjang member ditemukan
        total_harga = sum(barang['HARGA'] for barang in keranjang_member)                                               # Menghitung total harga dari variabel harga dikeranjang
        print(f"Keranjang {usernamelog[0]}:")
        for barang in keranjang_member:                                                                                 # Perulangan untuk menampilkan data keranjang member
            print(f"{barang['KODE']} - {barang['NAMA']} - Rp. {barang['HARGA']:,.0f} - Jumlah: {barang['JUMLAH']}")
        print(f"Total Harga: Rp. {total_harga:,.0f}")
        harga_dikeranjang["harganya"] = total_harga                                                                     # Menyimpan total harga ke variabel harga di keranjang
    else:                                                                                                               # Jika data keranjang member tidak ditemukan
        print("Keranjang kosong.")

def ubah_jumlah_barang():
    print("\n====================| Mengubah Jumlah Barang |===================")
    keranjang_member = [barang for barang in keranjang if barang.get('USERNAME', '') == usernamelog[0]]                             # Mengambil data keranjang berdasarkan username (keranjang member)
    if keranjang_member:                                                                                                            # Jika data keranjang member ditemukan
        tampilkan_katalog()
        while True:                                                                                                                 # Perulangan untuk sampai perulangan diberhentikan
            kode_ubah = input("\nSilakan pilih barang (kode barang) yang ingin diubah jumlahnya atau tekan ENTER untuk kembali: ")  
            if kode_ubah == "":                                             
                clears()    
                return                                                                                                              # Mengembalikan fungsi
            else:
                try:                                                                                                                # Untuk mengantisipasi kesalahan input                                                                                                            
                    kode = int(kode_ubah)                                                                                           # Mengubah inputan angka menjadi integer   
                    barang_ubah = next((barang_item for barang_item in keranjang if barang_item['KODE'] == kode), None)             # Mencari barang di variabel keranjang berdasarkan kode
                    if barang_ubah is not None:                                                                                     # Jika barang ditemukan
                        item = next((barang_item for barang_item in barang if barang_item['KODE'] == kode), None)                   # Mencari barang di variabel barang berdasarkan kode
                        if item is not None:                                                                                        # Jika barang ditemukan
                            item['STOK'] += barang_ubah['JUMLAH']                                                                   # Menambahkan stok barang
                            jumlah_baru = int(input("Masukkan jumlah barang baru: "))
                            if item['STOK'] >= jumlah_baru and jumlah_baru > 0:                                                     # Jika stok mencukupi dan jumlah inputan barang lebih dari 0
                                item['STOK'] -= jumlah_baru                                                                         # Mengurangi stok
                                barang_ubah['JUMLAH'] = jumlah_baru                                                                 # Mengubah jumlah
                                barang_ubah['HARGA'] = item['HARGA']                                                                # Mengubah harga
                                if jumlah_baru == 1:                                                                                # Jika jumlah inputan 1
                                    print(greenc, f"Jumlah {barang_ubah['NAMA']} telah diubah menjadi {jumlah_baru}.", whitec)
                                else:                                                                                               # Jika jumlah inputan lebih dari 1
                                    barang_ubah['HARGA'] *= jumlah_baru
                                    print(greenc, f"Jumlah {barang_ubah['NAMA']} telah diubah menjadi {jumlah_baru}.", whitec)  
                            elif jumlah_baru == 0:                                                                                  # Jika jumlah inputan 0
                                print(redc, "(!) Jumlah barang tidak boleh 0.", whitec)          
                            else:                                                                                                   # Jika stok tidak mencukupi
                                print("Stok barang tidak mencukupi.")
                        else:                                                                                                       # Jika barang tidak ditemukan
                            print(redc, "(!) Kode barang tidak valid.", whitec)
                    else:                                                                                                           # Jika barang tidak ditemukan
                        print(redc, "(!) Kode barang tidak valid.", whitec)
                except ValueError:                                                                                                  # Jika inputan bukan angka
                    print(redc, "(!) Masukkan kode barang yang valid.", whitec)
    else:                                                                                                                           # Jika data keranjang member tidak ditemukan
        print("Keranjang kosong.")
        lanjutan()

def hapus_dari_keranjang():                                                                                                         # Fungsi hapus dari keranjang
    print("\n====================| Menghapus Barang dari Keranjang |===================")
    keranjang_member = [barang for barang in keranjang if barang.get('USERNAME', '') == usernamelog[0]]                             # Mengambil data keranjang berdasarkan username (keranjang member)
    if keranjang_member:                                                                                                            # Jika data keranjang member ditemukan
        cek_keranjang()
        while True:                                                                                                                 # Perulangan sampai perulangan diberhentikan
            try:                                                                                                                    # Untuk mengantisipasi kesalahan input
                kode = (input("Masukkan kode barang yang ingin dihapus dari keranjang atau tekan ENTER untuk kembali: "))
                if kode == "":                                              
                    clears()
                    return
                else:                                                                                                              
                    kode = int(kode)                                                                                                # Mengubah inputan angka menjadi integer
                    barang_hapus = next((barang_item for barang_item in keranjang_member if barang_item['KODE'] == kode), None)     # Mencari barang di keranjang member berdasarkan kode
                    if barang_hapus is not None:                                                                                    # Jika barang ditemukan
                        i = 0                                                                                                       # Inisialisasi variabel i untuk iterasi perulangan
                        item = next((barang_item for barang_item in barang if barang_item['KODE'] == kode), None)                   # Mencari barang yang akan dihapus dari keranjang
                        if item is not None:                                                                                        # Jika barang ditemukan
                            item['STOK'] += barang_hapus['JUMLAH']                                                                  # Mengurangi stok
                            print(greenc, f"{item['NAMA']} telah dihapus dari keranjang.", whitec)
                            del keranjang[i]                                                                                        # Menghapus barang dari keranjang berdasarkan index
                        i += 1                                                                                                      # Tambahkan nilai i sebanyak 1 untuk melanjutkan iterasi
                    else:                                                                                                           # Jika barang tidak ditemukan
                        print(redc, "(!) Kode barang tidak valid.", whitec)
            except ValueError:                                                                                                      # Jika inputan bukan angka
                print(redc, "(!) Masukkan kode barang yang valid.", whitec)
    else:                                                                                                                           # Jika data keranjang member tidak ditemukan
        print("Keranjang kosong.")
        lanjutan()  

def bayar():
    print("\n====================| Pembayaran |===================")
    if keranjang:                                                                                  # Jika ada barang di keranjang
        cek_keranjang()
        print("(Sebagai member, anda mendapat diskon 10% !!!)")
        total_harga = harga_dikeranjang['harganya']                                                # Mengambil variabel barang_dikeranjang menjadi total harga                    
        if total_harga > 0:                                                                        # Jika total harga lebih dari 0
            diskon = total_harga * 0.10                                                            # Menghitung diskon
            total_harga_diskon = total_harga - diskon                                              # Total harga setelah diskon
            print(f"Diskon: Rp. {diskon:0,.0f}")
            print(f"Total Harga Setelah Diskon: Rp. {total_harga_diskon:0,.0f}")
            print("=====================================================")
            while True:                                                                            # Perulangan sampai perulangan diberhentikan
                try:                                                                               # Mengantisipasi kesalahan input
                    uang_bayar = int(input("Masukkan uang yang ingin dibayarkan: Rp. "))
                    if uang_bayar >= total_harga_diskon:                                           # Jika uang bayar cukup
                        print(f"Uang yang anda bayarkan adalah Rp {uang_bayar:,.0f}")              
                        kembalian = uang_bayar - total_harga_diskon                                # Menghitung kembalian
                        print(f"Kembalian yang harus anda terima adalah Rp {kembalian:,.0f}")
                        rekam_transaksi(keranjang.copy(), total_harga_diskon)                                          # Menduplikat keranjang lalu masukkan ke rekam transaksi
                        keranjang.clear()                                                          # Menghapus isi keranjang
                        harga_dikeranjang.clear()                                                  # Menghapus harga di harga_dikeranjang
                        print("Terima kasih telah berbelanja.")
                        break                                                                      # Menghentikan perulangan
                    else:                                                                          # Jika uang bayar tidak cukup
                        print("Uang yang anda bayarkan tidak cukup.")
                except ValueError:                                                                 # Jika inputan bukan angka
                    print(redc, "(!) Input uang harus berupa angka.", whitec)
    else:                                                                                          # Jika keranjang tidak ditemukan
        print("Keranjang Anda kosong.")

# ==================================================================================
# FUNGSI UNTUK MENU MEMBER
def tambah_barang():                                                                            # Fungsi untuk menambahkan data barang baru
    print("\n===== Menambahkan Data Barang =====")
    while True:                                                                                 # Perulangan sampai perulangan diberhentikan
        try:                                                                                    # Keyword untuk mengantisipasi bila ada kesalahan
            print("Data barang baru")
            nama = str(input("Nama barang : "))                                                 # Admin diminta menambahkan nama barang
            kode = int(input("Kode barang : "))                                                 # Admin diminta menambahkan kode barang
            if kode in [k['KODE'] for k in barang]:
                print(redc, "(!) Kode sudah ada.", whitec)
            else :                                                                              # Jika kode belum ada
                if kode < 0:                                                                    # Jika kode lebih kecil dari 0
                    print(redc, "(!) Kode harus lebih dari 0.", whitec)
                else:                                                                           # Jika kode lebih dari 0
                    harga = int(input("Harga barang : "))
                    if harga < 0:                                                               # Jika harga lebih kecil dari 0
                        print(redc, "(!) Harga harus lebih dari 0.", whitec)                    # Admin diminta menambahkan harga barang
                    else:                                                                       # Jika harga lebih dari 0
                        stock = int(input("Stok barang : "))  
                        if stock < 0:                                                           # Jika stok lebih kecil dari 0
                            print(redc, "(!) Stok harus lebih dari 0.", whitec)                 # Admin diminta menambahkan stock barang
                        else:                                                                   # Jika stok lebih dari 0
                            barang.append({"NAMA":nama,"HARGA":harga,"KODE":kode,"STOK":stock}) # Memanmbahkan data barang baru ke dalam list barang
                            print(greenc, "Data barang berhasil ditambahkan", whitec)
                            break                                                               # Menghentikan perulangan
        except ValueError:                                                                      # Jika inputan bukan angka
            print(redc, "(!) Inputan harus berupa angka", whitec)                           
        

def tampilkan_barang():
    print("\nKatalog Barang:")
    format_align = ["center", "center", "center", "center"]                                     # Mengatur format align tabel
    barang_copy = [item.copy() for item in barang]                                              # Menduplikat barang menjadi barang_copy untuk diformat
    for item in barang_copy:                                                                    # Perulangan untuk format harga
        item['HARGA'] = f"RP. {item['HARGA']:,.0f}"                                             # Mengubah format angka menjadi format rupiah
    print(tabulate(barang_copy, headers="keys", tablefmt="fancy_grid", colalign=format_align))  # Menampilkan tabel menggunakan tabulate

def update_barang():
    tampilkan_barang()
    print("\n===== Mengubah Data Barang =====")
    while True:                                                                                         # Perulangan sampai perulangan diberhentikan
        try:                                                                                            # Mengantisipasi kesalahan inputan
            pilihan = (input("Update stok (s) atau ubah data barang (u), (s/u) : "))
            if pilihan == "s":
                kode = int(input("Kode yang ingin diubah : "))
                item = next((barang_item for barang_item in barang if barang_item['KODE'] == kode), None)   # Mencari item berdasarkan kode di barang
                if item is not None:                                                                        # Jika item ditemukan
                    stok_baru = int(input("Ubah stok : "))
                    if stok_baru < 0:                                                                       # Jika stok harus lebih dari 0
                        print(redc, "(!) Stok harus lebih dari 0.", whitec)
                    else:                                                                                   # Jika stok lebih dari 0
                        item["STOK"] = stok_baru                                                            # Mengubah stok barang dengan stok yang baru
                        print(greenc, "Stok berhasil diubah.", whitec)
                        break
                else:                                                                                       # Jika item tidak ditemukan
                    print(redc, "(!) Kode tidak ditemukan.", whitec)
            elif pilihan == "u":
                kode = int(input("Kode yang ingin diubah : "))                  
                item = next((barang_item for barang_item in barang if barang_item['KODE'] == kode), None)   # Mencari item berdasarkan kode di barang
                if item is not None:                                                                        # Jika item ditemukan
                    print("Data barang baru")
                    nama_baru = str(input("Ubah nama : "))
                    item["NAMA"] = nama_baru                                                                # Mengubah nama barang dengan nama yang baru
                    kode_baru = int(input("Ubah kode : "))
                    if kode_baru in [k['KODE'] for k in barang]:                                            # Jika kode sudah ada
                        print(redc, "(!) Kode sudah ada.", whitec)
                    elif kode_baru < 0:                                                                     # Jika kode belum ada
                        item["KODE"] = kode_baru                                                            # Mengubah kode barang dengan kode yang baru
                        harga_baru = int(input("Ubah harga : "))
                        if harga_baru < 0:                                                                  # Jika harga harus lebih dari 0
                            item["HARGA"] = harga_baru                                                      # Mengubah harga barang dengan harga yang baru
                            stok_baru = int(input("Ubah stok : "))
                            if stok_baru < 0:                                                               # Jika stok harus lebih dari 0
                                item["STOK"] = stok_baru                                                    # Mengubah stok barang dengan stok yang baru
                                print(greenc, "Data barang telah diubah.", whitec)
                                break                                                                       # Menghentikan perulangan                           
                            else:
                                print(redc, "(!) Stok harus lebih dari 0.", whitec)
                        else:
                            print(redc, "(!) Harga harus lebih dari 0.", whitec)
                    else:
                        print(redc, "(!) Kode harus lebih dari 0.", whitec)
                else:                                                                                       # Jika item tidak ditemukan
                    print("Kode barang tidak ditemukan di keranjang.")
            else:
                print(redc, "(!) Inputan harus berupa 's' atau 'u'.", whitec)
        except ValueError:                                                                              # Jika inputan bukan angka
            print(redc, "(!) Kode yang dimasukkan bukan angka. Masukkan angka yang valid.", whitec)

def hapus_barang():                                                                                     # Fungsi untuk menghapus barang
    tampilkan_barang()
    print("\n===== Menghapus Data Barang ===== ") 
    while True:                                                                                         # Perulangan sampai pengguna memberikan kode yang sesuai
        try:                                                                                            # Keyword untuk mengantisipasi bila ada kesalahan
            kode = int(input("Kode : "))                                                                        
            item = next((barang_item for barang_item in barang if barang_item['KODE'] == kode), None)   # Membuat perulanganing untuk mengeluarkan value dictionary dari list ke variabel item
            if item is not None:                                                                        # Mencocokkan kode inputan user dengan kode yang ada dalam variabel item
                barang.remove(item)                                                                     # Menghapus data barang yang dipilih sesuai kode dalam variabel item
                print(greenc, f"Data dengan kode {kode} telah dihapus", whitec)
                break                                                                                   # Sebagai fungsi untuk mengeluarkan dari perulanganing
            else:                                                                                       # Kondisi jika item tidak ditemukan
                print(f"Tidak ada barang dengan kode {kode}")                                  
        except ValueError:                                                                              # Keyword untuk menerima kesalahan dari fungsi try dan mengatasinya
            print(redc, "(!) Kode yang dimasukkan bukan angka. Masukkan angka yang valid.", whitec)

def rekam_transaksi(keranjang, total_harga_diskon):                               # Fungsi untuk merekam transaksi
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                 # Mengambil waktu Sekarang
    
    total_harga = harga_dikeranjang['harganya']                                   # Cek harga yang ada di variabel harga_dikeranjang
    harga_didiskon = total_harga_diskon                                           # Cek harga yang ada di variabel total_harga_diskon

    transaksi = {                                                                 # Membuat dictionary transaksi
        'Waktu': waktu_sekarang,                                                  # Menambahkan waktu sekarang ke value waktu 
        'Barang': keranjang,                                                      # Menambahkan barang yang dibeli ke value barang
        'Total Harga': total_harga,                                               # Menambahkan total harga ke value total harga 
        'Hargadidiskon' : harga_didiskon,                                         # Menambahkan harga didiskon ke value harga didiskon
        'Username': usernamelog[0]                                                # Menambahkan username ke value username
    }
    riwayat_pembelian.append(transaksi)                                           # Menambahkan transaksi ke list riwayat_pembelian

def lihat_riwayat_pembelian():
    print("\n===== Riwayat Belanja Member =====")
    if riwayat_pembelian:                                                                                   # Jika ada riwayat transaksi
        for transaksi in riwayat_pembelian:                                                                 # Perulangan untuk menampilkan riwayat transaksi
            print(f"Waktu: {transaksi['Waktu']}")
            if 'Barang' in transaksi:                                                                       # Jika ada barang yang dibeli
                print("Barang yang dibeli:")
                for barang in transaksi['Barang']:                                                          # Perulangan untuk menampilkan barang yang dibeli
                    print(f"  - {barang['NAMA']} ({barang['JUMLAH']} pcs) - Rp. {barang['HARGA']:,.0f}")
            else:                                                                                           # Jika tidak ada barang yang dibeli
                print("Tidak ada informasi barang yang dibeli.")
            print(F"Mendapat diskon sebesar 10%")
            print(f"Total Harga: RP.{transaksi['Total Harga']:,.0f}")
            print(f"Total harga setelah diskon: RP.{transaksi['Hargadidiskon']:,.0f}")
            print(f"Username: {transaksi['Username']}")
            print("=" * 50)
    else:                                                                                                   # Jika tidak ada riwayat transaksi
        print("Tidak ada riwayat transaksi.")
    
# FUNGSI MENU
def menu_member():                                                                      # Fungsi menu member
    while True:                                                                         # Perulangan sampai pengguna memberikan pilihan lalu break
        print("""==========| MENU MEMBER |==========                 
1. Isi keranjang
2. Cek keranjang
3. Ubah jumlah barang
4. Hapus barang di keranjang
5. Bayar
6. Logout akun
===================================""")
        pilih = input("\nMasukkan nomor operasi yang ingin anda lakukan: ")

        if pilih == "1":                                                                # Isi keranjang
            isi_keranjang()
        elif pilih == "2":                                                              # Cek keranjang
            cek_keranjang()
            lanjutan()
        elif pilih == "3":                                                              # Ubah jumlah barang
            ubah_jumlah_barang()
        elif pilih == "4":                                                              # Hapus barang di keranjang
            hapus_dari_keranjang()
        elif pilih == "5":                                                              # Bayar
            bayar()
            lanjutan()
        elif pilih == "6":                                                              # Logout akun
            print(f"Sampai Jumpa, {usernamelog[0]}!")
            time.sleep(2)
            break                                                                       # Menghentikan perulangan
        else:                                                                           # Pilihan tidak tersedia
            print(redc, "(!) Pilihan tidak tersedia. Silakan pilih kembali.", whitec)
            time.sleep(2)
            clears()
    
def menu_admin():                                                                       # Fungsi menu admin
    while True:                                                                         # Perulangan sampai pengguna memberikan pilihan lalu break
        print("""==========| MENU ADMIN |==========
1. Menambahkan data barang 
2. Tampilkan data barang
3. Memperbarui data barang
4. Hapus data barang
5. Riwayat pembelian member
6. Logout akun
==================================""")
        pilih = input("\nMasukkan nomor operasi yang ingin anda lakukan: ")

        if pilih == "1":                                                                # Menambahkan data
            tambah_barang()
            time.sleep(2)                                                               # Delay waktu untuk 2 detik
            clears()
        elif pilih == "2":                                                              # Tampilkan data
            tampilkan_barang()
            lanjutan()
        elif pilih == "3":                                                              # Memperbarui data
            update_barang()
            time.sleep(2)                                                               # Delay waktu untuk 2 detik
            clears()
        elif pilih == "4":                                                              # Hapus data
            hapus_barang()
            time.sleep(2)                                                               # Delay waktu untuk 2 detik
            clears()
        elif pilih == "5":                                                              # Riwayat pembelian
            lihat_riwayat_pembelian()
            lanjutan()
        elif pilih == "6":                                                              # Logout akun
            print("Sampai Jumpa, Admin!")
            time.sleep(2)                                                               # Delay waktu untuk 2 detik
            break                                                                       # Menghentikan perulangan
        else:                                                                           # Pilihan tidak tersedia
            print(redc, "(!) Pilihan tidak tersedia. Silakan pilih kembali.", whitec)
            time.sleep(2)                                                               # Delay waktu untuk 2 detik
            clears()

def menu_akun():                                                                        # Fungsi menu akun
    while True:                                                                         # Perulangan sampai pengguna memberikan pilihan lalu break
        clears()
        print("+-----------------+")
        print("|  TOKO FURNITUR  |")
        print("+-----------------+")
        print("===| MENU AKUN |===")            
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        print("===================")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":                                                              # Register
            register()
            time.sleep(2)                                                               # Delay waktu untuk 2 detik
        elif pilihan == "2":                                                            # Login
            login()
            if admin == True:                                                           # Jika login berhasil dan admin = True
                time.sleep(2)
                clears()
                menu_admin()
            else:                                                                       # Jika login berhasil dan admin = False
                time.sleep(2)
                clears()
                menu_member()
        elif pilihan == "3":                                                            # Keluar
            print("Terima Kasih Telah Menggunakan Layanan Kami")
            time.sleep(2)                                                               # Delay waktu untuk 2 detik
            exit()
        else:                                                                           # Pilihan tidak tersedia
            print(redc, "(!) Pilihan tidak tersedia. Silakan pilih kembali.", whitec)
            time.sleep(2)                                                               # Delay waktu untuk 2 detik

menu_akun()                                                                             # Memanggil fungsi menu_akun
