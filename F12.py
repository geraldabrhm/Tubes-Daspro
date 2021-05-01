# ============================ F12 ========================================
def riwayatKembali():
    rolling = True
    count = 0
    while rolling:
        returnSort = sorted(gadget_return_history[count+1:], key = lambda date: datetime.datetime.strptime(date[2], '%d/%m/%Y'),reverse=True)
        lanjutkan = True
        for i in range(5):
            try:
                #cari id gadget dan id user
                for line in range(len(gadget_borrow_history)):
                    if returnSort[i][1] == gadget_borrow_history[line][0]:
                        id_gadget = gadget_borrow_history[line][2]
                        id_user = gadget_borrow_history[line][1]

                namaUser = user[cariID(user,id_user)][2]
                namaGadget = gadget[cariID(gadget,id_gadget)][1]

                print()
                print("ID Pengembalian      : " + returnSort[i][0])
                print("Nama Pengambil       : " + namaUser)
                print("Nama Gadget          : " + namaGadget)
                print("Tanggal Pengembalian : " + returnSort[i][2])
                print("Jumlah               : " + str(returnSort[i][3]))
            except:
                # Ketika data habis maka akan terjadi IndexError
                IndexError
                print()
                print("Data sudah habis")
                lanjutkan = False
                break
        if lanjutkan and len(returnSort) != 5:
            print()
            nextInp = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
            # Validasi input
            while not validasiYN(nextInp):
                nextInp = input("Apakah mau ditampilkan data lebih lanjut? (Y/N) ")
            if nextInp == 'Y':
                count += 5
            else:
                rolling = False
        else:
            rolling = False