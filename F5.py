# ============================ F5 ========================================
def tambahItem():
    # Menambahkan data item baru ke database

    # input ->  gadget, consumable : array of array of string and integer
    # output -> gadget, consumable : array of array of string and integer
    
    # I.S. : matriks data gadget dan consumable telah terdefinisi
    # F.S. : data item baru dimasukkan ke dalam database

    # KAMUS LOKAL
    # lanjut : boolean

    # Function / Procedure
    # IDItemAda(data : array of array of string and integer, ID : string) -> boolean
    # Mengecek apakah ID ada pada data
    # I.S. data dan ID terdefinisi
    # F.S. Mengembalikan True jika ID item ada di data dan False jika sebaliknya

    # ALGORITMA
    # Validasi ID
    lanjut = False
    while not lanjut:
        print()
        ID = input("Masukkan ID: ")
        if (ID[0] == 'G'):
            if IDItemAda(gadget,ID):
                print("Gagal menambahkan item karena ID sudah ada.")
            else:
                lanjut = True
        elif (ID[0] == 'C'):
            if IDItemAda(consumable,ID):
                print("Gagal menambahkan item karena ID sudah ada.")
            else:
                lanjut = True
        else:
            # asumsi ID diawali huruf besar (kapitalisasi benar)
            print("Gagal menambahkan item karena ID tidak valid.")

    nama = input("Masukkan Nama: ")
    deskripsi = input("Masukkan Deskripsi: ")
    
    # Validasi jumlah
    isNumber = False
    while not isNumber:
        jumlah = input("Masukkan Jumlah: ")
        try:
            jumlah = int(jumlah)
            if jumlah <= 0:
                print("Jumlah harus bernilai positif")
            else:
                isNumber = True
        except:
            ValueError
            print("Jumlah harus berupa bilangan integer, silakan masukkan kembali")
            print()
    
    # Validasi rarity
    isRarity = False
    while not isRarity:
        rarity = input("Masukkan Rarity: ")
        if rarity in "CBAS":
            isRarity = True
        else:
            print("Rarity harus berupa karakter C, B, A, atau S")
            print()
    
    arrTambahItem = [ID,nama,deskripsi,jumlah,rarity]
    if ID[0] == 'G':
        
        # Validasi tahun
        isTahun = False
        while not isTahun:
            tahun = input("Masukkan tahun ditemukan: ")
            try:
                tahun = int(tahun)
                break
            except:
                ValueError
                print("Tahun harus berupa bilangan integer, silakan masukkan kembali")
                print()
            # isTahun == True

        arrTambahItem.append(tahun)
        gadget.append(arrTambahItem)
    else:
        consumable.append(arrTambahItem)
    
    print("Item telah berhasil ditambahkan ke database.")