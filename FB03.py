# ============================ FB03 ========================================
def seed(seed):
    global random
    random = round(time.time())

def rand():
    a = 47071034
    c = 22206856
    m = 87635214759
    global random
    random = (a*random + c) % m
    return random

def chance(lstRarity,rarity):
    if rarity == 'C':
        lstRarity[0] += 90
        lstRarity[1] += 10
    elif rarity == 'B':
        lstRarity[0] += 10
        lstRarity[1] += 80
        lstRarity[2] += 10
    elif rarity == 'A':
        lstRarity[1] += 10
        lstRarity[2] += 80
        lstRarity[3] += 10
    else:
        lstRarity[2] += 10
        lstRarity[3] += 90
    sum = 0
    for i in range(4):
        sum += lstRarity[i]
    for i in range(4):
        lstRarity[i] = lstRarity[i] * 100 / sum

    return lstRarity

def printChance(chance,rarity):
    if chance != 0:
        return Bold(rarity) + " (" + Bold("{:.2f}".format(chance)) + "%) "
    else:
        return ""

def hasilGacha(lstChance):
    random = rand() % 100 # 0 - 99
    random += 1
    for i in range(4):
        random -= lstChance[i]
        if random <= 0:
            if i == 0:
                return 'C'
            elif  i == 1:
                return 'B'
            elif i == 2:
                return 'A'
            else:
                return 'S'

def Gacha():
    global lstChance
    global inventory_user
    global consumable
    
    print()
    print("========INVENTORY========")
    count = 0
    IDInventory = []
    for i in range(len(inventory_user)):
        if inventory_user[i][0] == idUser:
            count += 1

def gacha():
    global lstChance
    global inventory_user
    global consumable_history
    global consumable
    
    print()
    print("========INVENTORY========")
    count = 0
    IDInventory = []
    for i in range(len(inventory_user)):
        if inventory_user[i][0] == idUser:
            count += 1
            urutan = cariID(consumable,inventory_user[i][1])
            print(str(count) + ". " + consumable[urutan][1] + "(Rarity " + consumable[urutan][4] + ") (" + str(inventory_user[i][2]) + ")")
            IDInventory.append(inventory_user[i][1])
    if count == 0:
        print("Anda tidak mempunyai consumable di inventory Anda")
        print("=========================")
        print()
        return
    print("=========================")
    print()
    
    # Validasi consumable yang digunakan
    digunakanBenar = False
    while not digunakanBenar:
        try:
            digunakan = int(input("Pilih consumable yang mau digunakan: "))
            if digunakan > count:
                print("Input anda tidak valid")
                print()
            else:
                digunakanBenar = True
        except:
            ValueError
            print("Pilihan harus berupa bilangan bulat")
            print()
    urutanInventory = cariData(inventory_user,IDInventory[digunakan-1],1)

    # Validasi jumlah consumable yang digunakan
    jumlahBenar = False
    while not jumlahBenar:
        try:
            jumlah = int(input("Jumlah yang digunakan: "))
            if jumlah > inventory_user[urutanInventory][2]:
                print("Jumlah yang diinputkan terlalu banyak")
                print()
            else:
                jumlahBenar = True
        except:
            ValueError
            print("Pilihan harus berupa bilangan bulat")
            print()

    urutan = cariID(consumable,IDInventory[digunakan - 1])
    consumable[urutan][3] += jumlah
    inventory_user[urutanInventory][2] -= jumlah
    if inventory_user[urutanInventory][2] == 0:
        inventory_user.pop(urutanInventory)
    print(Bold(consumable[urutan][1]) + " (" + Bold("x" + str(jumlah)) + ") ditambahkan!")
    lstChance = chance(lstChance,consumable[urutan][4])

    print("Chance mendapatkan Rarity ", end='')
    if lstChance[0] != 0:
        print(Bold('C') + " (" + Bold("{:.2f}".format(lstChance[0])) + "%) ", end='')
    if lstChance[1] != 0:
        print(Bold('B') + " (" + Bold("{:.2f}".format(lstChance[1])) + "%) ", end='')
    if lstChance[2] != 0:
        print(Bold('A') + " (" + Bold("{:.2f}".format(lstChance[2])) + "%) ", end='')
    if lstChance[3] != 0:
        print(Bold('S') + " (" + Bold("{:.2f}".format(lstChance[3])) + "%)", end='')
    print()
    print()
    perintah = input("Tambahkan item lagi? (Y/N): ")
    
    # Validasi perintah
    while not validasiYN(perintah):
        perintah = input("Tambahkan item lagi? (Y/N): ")
    
    if perintah == 'Y':
        gacha()
    else:
        print()
        print("Rolling...")
        time.sleep(3)
        print()
        rarity = hasilGacha(lstChance)        
        finished = False
        while not finished:
            for i in range(len(consumable)):
                if consumable[i][4] == rarity:
                    print("Selamat Anda mendapatkan " + Bold(consumable[i][1]) + " (Rarity " + rarity + ") sebanyak x" + Bold(str(consumable[i][3])) + "!")
                    tambah_con_history = ["CH" + str(len(consumable_history)),idUser,consumable[i][0],datetime.date.today().strftime("%d/%m/%Y"),consumable[i][3]]
                    consumable_history.append(tambah_con_history)
                    tambah_inventory = [idUser,consumable[i][0],consumable[i][3]]
                    inventory_user.append(tambah_inventory)
                    consumable[i][3] = 0
                    lstChance = [0,0,0,0]
                    finished = True
                    return
            rarity = hasilGacha(lstChance)