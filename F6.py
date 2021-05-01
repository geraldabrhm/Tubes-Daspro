# ============================ F6 ========================================
def hapusItem():
    # Menghapus gadget dari database
    
    # input / output -> gadget : array of array of string and integer
    
    # I.S. matriks data gadget terdefinisi
    # F.S. data yang diinputkan dihapus dari data gadget
    
    # KAMUS LOKAL
    # ID : string
    # urutan : integer
    
    # Function / Procedure
    # validasiYN(jawaban : string) -> boolean
    # Memvalidasi input dari user, harus 'Y' atau 'N'
    # I.S. string terdefinisi
    # F.S. mengembalikan True jika string adalah 'Y' atau 'N' dan False jika sebaliknya

    # IDItemAda(data : array of array of string and integer, ID : string) -> boolean
    # Mengecek apakah ID ada pada data
    # I.S. data dan ID terdefinisi
    # F.S. Mengembalikan True jika ID item ada di data dan False jika sebaliknya
    
    # ALGORITMA
    # Validasi ID
    rolling = True
    while rolling:
        print()
        ID = input("Masukkan ID item: ")
        if ID[0] == 'G':
            if IDItemAda(gadget,ID):
                urutan = cariID(gadget,ID)
                jawaban = input("Apakah anda yakin ingin menghapus " + gadget[urutan][1] + " (Y/N)? ")
                
                # Validasi jawaban
                while not validasiYN(jawaban):
                    jawaban = input("Apakah anda yakin ingin menghapus " + gadget[urutan][1] + " (Y/N)? ")
                    
                if jawaban == 'Y':
                    gadget.pop(urutan)
                    print()
                    print("Item telah berhasil dihapus dari database.")
                else:
                    print("Item tidak jadi dihapus dari database")
                rolling = False
            else:
                print("Tidak ada item dengan ID tersebut.")
        elif ID[0] == 'C':
            if IDItemAda(consumable,ID):
                urutan = cariID(consumable,ID)
                jawaban = input("Apakah anda yakin ingin menghapus " + consumable[urutan][1] + " (Y/N)? ")

                # Validasi jawaban
                while not validasiYN(jawaban):
                    jawaban = input("Apakah anda yakin ingin menghapus " + gadget[urutan][1] + " (Y/N)? ")

                if jawaban == 'Y':
                    consumable.pop(urutan)
                    print()
                    print("Item telah berhasil dihapus dari database.")
                else:
                    print("Item tidak jadi dihapus dari database")
                rolling = False
            else:
                print("Tidak ada item dengan ID tersebut.")
        else:
            print("Tidak ada item dengan ID tersebut.")
    # rolling == False