import fungsi as f

menu = {
    "1": f.lihat,   "l" : f.lihat,
    "2": f.tambah,  "t" : f.tambah,
    "3": f.ubah,    "u" : f.ubah,
    "4": f.hapus,   "h" : f.hapus,
    "5": f.cari,    "c" : f.cari,
    "6": exit,      "k" : exit
}

r = "\033[0m"
h = "\033[1;32m"
b = "\033[1;34m"
m = "\033[1;31m"
k = "\033[1;33m"
u = "\033[1;35m"
p = "\033[1;37m"

while True:
    print(
        f"{p}L{r}ihat |", 
        f"{h}T{r}ambah |", 
        f"{b}U{r}bah |", 
        f"{m}H{r}apus |", 
        f"{k}C{r}ari |", 
        f"{u}K{r}eluar"
    )
    pilihan = input("Masukkan pilihan: ").lower()
    if pilihan in menu:
        menu[pilihan]()
    else:
        print("Pilihan tidak ada.")