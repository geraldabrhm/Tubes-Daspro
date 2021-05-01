# ============================ F14 ========================================
def load_data(file):
    f = open(file,"r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    lstAll = []
    for line in lines:
        lst = []
        data =""
        for i in range(len(line)):
            if line[i] == ';':
                lst.append(data)
                data = ""
            elif (i == len(line) - 1):
                lst.append(data + line[i])
            else:
                data += line[i]
        lstAll.append(lst)
    return lstAll

def tryInt(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            try:
                data[i][j] = int(data[i][j])
            except:
                ValueError
            if data[i][j] == "True":
                data[i][j] = True
            elif data[i][j] == "False":
                data[i][j] = False
    return data

def load(folder):
    global user
    global gadget
    global consumable
    global consumable_history
    global gadget_borrow_history
    global gadget_return_history
    global inventory_user
    
    os.chdir('./' + str(folder))
    
    user = load_data("user.csv")
    gadget = tryInt(load_data("gadget.csv"))
    consumable = tryInt(load_data("consumable.csv"))
    consumable_history = tryInt(load_data("consumable_history.csv"))
    gadget_borrow_history = tryInt(load_data("gadget_borrow_history.csv"))
    gadget_return_history = tryInt(load_data("gadget_return_history.csv"))
    inventory_user = tryInt(load_data("inventory_user.csv"))
    os.chdir('../')

def loading():
    parser = argparse.ArgumentParser(description="""
Program Tugas Besar IF1210 Kelompok 11 Kelas 10 Dasar Pemrograman
\033[93mformat input : python main.py -f <nama-folder-csv>\033[0m
""", epilog='Enjoy the program! :D')
    
    parser.add_argument("-f","--folder", type=str, help="Inputkan nama folder csv (harus diinputkan)")  
    if parser.parse_args().folder is None:
        parser.error("""
\033[91mNama folder csv tidak diinputkan!\033[0m
\033[93mformat input : python main.py -f <nama-folder-csv>\033[0m""")
        return None
    
    directory = parser.parse_args().folder
    parent = os.getcwd()
    path = os.path.join(parent, directory)
    if not os.path.exists(path):
        print("Nama folder yang diinputkan tidak ada")
    else:
        os.chdir('./' + directory)
        lstFile = ["user.csv","gadget.csv","gadget_borrow_history.csv","gadget_return_history.csv","consumable.csv","consumable_history.csv"]
        for files in lstFile:
            if not fileExist(files):
                print(files + " tidak tersedia di folder yang diinputkan")
                return None
        if not fileExist('inventory_user.csv'):
            print(colorStr("file inventory_user.csv tidak tersedia, program tetap bisa berjalan tetapi tidak dengan opsi gacha"))
        os.chdir('../')
        return directory
        
def fileExist(files):
    if os.path.exists(files):
        return True
    else:
        return False