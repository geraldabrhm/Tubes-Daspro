# ============================ FUNGSI TAMBAHAN ========================================

# Mengembalikan string menjadi tulisan tebal
def Bold(string):
    hasil = "\033[1m" + string + "\033[0m"
    return hasil

# Mengubah data
def modify_data(data, idx, col, value):
    data[idx][col] = value
    return data

# Mencari data Item berdasarkan ID
def cariID(data,ID):
    for i in range(len(data)):
        if data[i][0] == ID:
            return i


def IDItemAda(data,ID):
    # Mengecek apakah ID ada pada data
    # I.S. data dan ID terdefinisi
    # F.S. Mengembalikan True jika ID item ada di data dan False jika sebaliknya
    
    # KAMUS LOKAL
    # Ada : boolean
    # i : integer
    
    # ALGORITMA
    Ada = False
    for i in range(len(data)):
        if data[i][0] == ID:
            return True
    return False

# Mencari data berdasarkan index (generalisasi cariID)
def cariData(data,dicari,index):
    for i in range(len(data)):
        if data[i][index] == dicari:
            return i

# Mengembalikan string menjadi string berwarna jika di-print
def colorStr(string,color):
    if color == "purple":
        warna = '\033[95m'
    elif color == "cyan":
        warna = '\033[96m'
    elif color == "darkcyan":
        warna = '\033[36m'
    elif color == "blue":
        warna = '\033[94m'
    elif color == "green":
        warna = '\033[92m'
    elif color == "yellow":
        warna = '\033[93m'
    elif color == "red":
        warna = '\033[91m'
    elif color == "bold":
        warna = '\033[1m'
    else:
        return string
    return warna + string + '\033[0m'

# Memvalidasi input tanggal
def tglValid(date):
    date_format = '%d/%m/%Y'
    try:
        datetime.datetime.strptime(date, date_format)
        return True
    except ValueError:
        return False

def validasiYN(string):
    # Memvalidasi input dari user, harus 'Y' atau 'N'
    # I.S. string terdefinisi
    # F.S. mengembalikan True jika string adalah 'Y' atau 'N' dan False jika sebaliknya
    
    # KAMUS LOKAL
    # string : string
    
    # ALGORITMA
    if (string == 'Y') or (string == 'N'):
        return True
    else:
        print("Jawaban harus 'Y' atau 'N' ")
        print()
        return False