# ============================ F10 ========================================
def mintaConsumable():
    ID = input("Masukkan ID item: ")
    # Validasi ID ada
    while not (cariID(consumable,ID) == None):
        print("ID item tidak tersedia, mohon inputkan ID yang benar")
        print()
        ID = input("Masukkan ID item: ")
        indexCon = cariID(consumable,ID)
    
    # Validasi jumlah
    jumlahCocok = False
    while not jumlahCocok:
        try:
            jumlah = int(input("Jumlah: "))
            if jumlah > consumable[indexCon][3]:
                print("Jumlah melebihi jumlah database")
                print()
            elif jumlah <= 0:
                print("Jumlah harus positif")
                print()
            else:
                jumlahCocok = True
        except ValueError:
            print("Jumlah harus berupa bilangan bulat, silakan input kembali")
            print()
    
    # Validasi tanggal
    tanggal = input("Tanggal permintaan: ")
    while not tglValid(tanggal):
        print("Tanggal yang diinputkan invalid, mohon inputkan kembali")
        print()
        tanggal = input("Tanggal permintaan: ")
    
    consumable[indexCon][3] -= jumlah
    tambahHistory = ["CH" + str(len(consumable_history)), idUser, ID, tanggal, jumlah]
    consumable_history.append(tambahHistory)
    dataInventory = cariData(inventory_user,ID,1)
    if dataInventory == None:
        tambahInventory = [idUser,ID,jumlah]
        inventory_user.append(tambahInventory)
    else:
        inventory_user[dataInventory][2] += jumlah
    
    print("Item " + Bold(consumable[indexCon][1] + " (x" + str(jumlah) + ")") + " telah berhasil diambil!")