# ============================ F13 ========================================
def riwayatConsumable():
    # Menampilkan daftar pengambilan consumable yang telah dilakukan para user ke layar
    
    # input ->  consumable_history : array of array of string and integer
    #           user : array of array of string
    #           consumable : array of list of string and integer
    
    # I.S. matriks data user, gadget, gadget_borrow_history terdefinisi
    # F.S. tercetak ke layar riwayat peminjaman user
    
    # KAMUS LOKAL
    # rolling, berikutnya : boolean
    # count : integer
    # consumableSort : array of list of integer and string
    # namaUser, namaConsumable : string
    
    # Function / Procedure
    # validasiYN(jawaban : string) -> boolean
    # Memvalidasi input dari user, harus 'Y' atau 'N'
    # I.S. string terdefinisi
    # F.S. mengembalikan True jika string adalah 'Y' atau 'N' dan False jika sebaliknya
    
    # ALGORITMA
    rolling = True
    count = 0
    while rolling:
        consumableSort = sorted(consumable_history[count+1:], key = lambda date: datetime.datetime.strptime(date[3], '%d/%m/%Y'),reverse=True)
        berikutnya = True
        for i in range(5):
            try:
                namaUser = user[cariID(user,consumableSort[i][1])][2]
                namaConsumable = consumable[cariID(consumable,consumableSort[i][2])][1]
                print()
                print("ID Pengambilan       : " + consumableSort[i][1])
                print("Nama Pengambil       : " + namaUser)
                print("Nama Consumable      : " + namaConsumable)
                print("Tanggal Pengambilan  : " + consumableSort[i][3])
                print("Jumlah               : " + str(consumableSort[i][4]))
            except:
                # Ketika data habis maka akan terjadi IndexError
                print(i)
                IndexError
                print()
                print("Data sudah habis")
                berikutnya = False
                break
        if berikutnya and len(consumableSort) != 5:
            print()
            nextInp = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
            # Validasi input
            while not validasiYN(nextInp):
                lanjut = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
            if nextInp == 'Y':
                count += 5
            else:
                rolling = False
        else:
            rolling = False