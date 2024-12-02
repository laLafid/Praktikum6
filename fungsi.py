import kotak as tb # pangil fungsi dari file tabel

mahadata = {} # Dictionary kosong
# nantinya akan di isi dengan data dari user

def nilai(str):
# fungsi untuk memastikan input adalah angka
# dan mengulangi permintaan jika input bukan angka
# juga membatasi nilai input yang diinputkan.
    while True:
        try:
            poin = float(input(str))
            if poin < 0 or poin > 100:
                print(f"Nilai harus berkisar dari 0 hingga 100.")
            else:
                return poin
        except ValueError:
            print("Input harus berupa angka!!")    
               
def namamu(str, harus_ada=True):
# fungsi ini akan meminta input nama dari user
# melihat apakah nama tersebut ada di database atau tidak
    while True:
        nama = input(str)
        if harus_ada and nama not in mahadata:
            print("nama tidak ditemukan!")
        elif not harus_ada and nama in mahadata:
            print("nama sudah ada di database. Masukkan nama lain!")
        else:
            return nama  
            
def minta(nama):
# fungsi minta input data``
# sekaligus melihat apakah data dengan nama yang sama ada di dictionary
    tugas, uts, uas = map(nilai, [
            "Masukkan Nilai Tugas: ", 
            "Masukkan Nilai UTS: ", 
            "Masukkan Nilai UAS: "
            ])
    akhir = (tugas*0.3) + (uts*0.35) + (uas*0.35)
    if nama not in mahadata:
        NIM = input("Masukkan NIM (e.g. 123456789): ")
        return {
            "Nama": nama,
            "NIM": NIM,
            "Nilai Tugas": tugas,
            "Nilai UTS": uts,
            "Nilai UAS": uas,
            "Nilai Akhir": akhir
        }
    elif nama in mahadata:
        return {
            "Nama": nama,
            "NIM": mahadata[nama]["NIM"], # NIM dari data lama
            "Nilai Tugas": tugas,
            "Nilai UTS": uts,
            "Nilai UAS": uas,
            "Nilai Akhir": akhir
        }
    
def tambah():
# fungsi yang akan menambahkan data yang sudah diterima fungsi minta
# ke dalam dictionary
    nama = namamu("Masukkan Nama: ",harus_ada=False)
    mahadata[nama] = minta(nama)
    print("Data berhasil ditambahkan.")
    
def ubah():
# fungsi akan mencari data dengan nama yang sesuai
# kemudian meminta input data baru
# input tersebut akan menggantikan data yang sudah ada
    nama = namamu("Masukkan Nama: ")
    mahadata[nama] = minta(nama)
    print("Data berhasil diubah.")
    
def hapus():
# fungsi ini gunanya untuk hapus data dari dictionary
    nama = namamu("Masukkan Nama: ")
    del mahadata[nama]
    print("Data berhasil dihapus.")
    
def lihat():
# fungsi untuk menampilkan data yang ada di dictionary
    tb.tabel(mahadata, title="Data Mahasiswa") 

def cari():
# akan mencari dengan nama
# data dengan nama tersebut akan ditamplikan kepada user
    nama = namamu("Masukkan Nama: ")
    tb.tabel({nama: mahadata[nama]}, title=f"Data Mahasiswa dengan Nama {nama}")