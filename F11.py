# ============================ F11 ========================================
def riwayatPinjam():
    # Menampilkan daftar peminjaman gadget yang telah dilakukan para user ke layar
    
    # input ->  gadget_borrow_history : array of array of string
    #           user : array of array of string
    #           gadget : array of list of string and integer
    
    # I.S. matriks data user, gadget, gadget_borrow_history terdefinisi
    # F.S. tercetak ke layar riwayat peminjaman user
    
    # KAMUS LOKAL
    # rolling, bisaLanjut : boolean
    # count : integer
    # borrowSort : array of list of integer and string
    # namaUser, namaGadget : string
    
    # Function / Procedure
    # validasiYN(jawaban : string) -> boolean
    # Memvalidasi input dari user, harus 'Y' atau 'N'
    # I.S. string terdefinisi
    # F.S. mengembalikan True jika string adalah 'Y' atau 'N' dan False jika sebaliknya
    
    # ALGORITMA
    rolling = True
    count = 0
    while rolling:
        borrowSort = sorted(gadget_borrow_history[count+1:], key = lambda date: datetime.datetime.strptime(date[3], '%d/%m/%Y'),reverse=True)
        bisaLanjut = True
        for i in range(5):
            try:
                namaUser = user[cariID(user,borrowSort[i][1])][2]
                namaGadget = gadget[cariID(gadget,borrowSort[i][2])][1]
                print()
                print("ID Peminjam          : " + borrowSort[i][1])
                print("Nama Pengambil       : " + namaUser)
                print("Nama Gadget          : " + namaGadget)
                print("Tanggal Peminjamanan : " + borrowSort[i][3])
                print("Jumlah               : " + str(borrowSort[i][4]))
            except:
                # Ketika data habis maka akan terjadi IndexError
                IndexError
                print()
                print("Data sudah habis")
                bisaLanjut = False
                break

        if bisaLanjut and len(borrowSort) != 5:
            print()
            lanjut = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
            # Validasi input
            while not validasiYN(lanjut):
                lanjut = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
            if lanjut == 'Y':
                count += 5
            else:
                rolling = False
        else:
            rolling = False