# ============================ F8 ========================================
def pinjam():
    # Meminjam gadget sesuai id_item yang dimasukan dan akan mengurangi jumlah pada gadget dan menambahkan entri pada gadget_borrow_history
    
    # input/output -> gadget : array of array of string and integer
    # input/output -> gadget_borrow_history : array of array of string, integer, and boolean
    
    # I.S. matriks data gadget dan gadget_borrow_history terdefinisi
    # F.S. jumlah gadget pada data gadget berkurang dan terdapat entri baru pada gadget_borrow_history
    
    # KAMUS LOKAL
    # id_item, id_peminjaman : string
    # condition, found, syarat_terpenuhi_1 : boolean
    # indeks, current_amount, amount : integer
    
    # ALGORITMA    
    # Validasi ID_Item
    condition = True
    while condition:
        try:
            id_item = input("Masukan ID item: ")
            found = False
        
            for i in range(1, len(gadget)):
                if gadget[i][0] == id_item:
                    found = True
                    condition = False
                    indeks = i
            if found == False:
                print("Tidak ada item dengan ID tersebut. Silahkan masukan kembali ID item yang sesuai")
                print()
        except ValueError:
            print()
    
    # Membuat array dari setiap gadget yang user pernah pinjam
    personal_borrow = []
    for a in range(len(gadget_borrow_history)):
        if gadget_borrow_history[a][1] == idUser:
            personal_borrow.append(gadget_borrow_history[a])
    
    # Mengecek apakah user pernah meminjam dan belum mengembalikan gadget yang sama atau user belum pernah meminjam sama sekali dari gadget dengan id_item
    # Syarat 1: User sudah mengembalikan gadget dengan id_item yang dimasukan secara utuh (tidak sebagian)
    syarat_terpenuhi_1 = False
    for i in range(len(personal_borrow)-1, 0, -1):
        if personal_borrow[i][2] == id_item:
            if personal_borrow[i][5] == True:
                syarat_terpenuhi_1 = True
                break
    # Syarat 2: User belum pernah sama sekali meminjam gadget dengan id_item inputan
    check = None
    for i in range(len(personal_borrow)):
        if personal_borrow[i][2] == id_item:
            check = 'Checked'
    
    # Jika user sudah pernah mengembalikan secara lengkap gadget dengan id = id_item (atau) gadget dengan id = id item belum pernah ia pinjam sama sekali
    if syarat_terpenuhi_1 == True or check == None:
        # Validasi Tanggal
        format = "%d/%m/%Y"
    
        while(True):
            date_string = input("Tanggal peminjaman: ").strip()
        
            try:
                datetime.datetime.strptime(date_string, format)
                break
            except ValueError:
                print("Tanggal yang anda masukan salah. Silahkan masukan kembali tanggal dengan format DD/MM/YYYY")
                print()
            
        # Validasi jumlah
        current_amount = gadget[indeks][3]
        terms = True
    
        while(terms):
            try:
                amount = int(input("Jumlah peminjaman: "))
        
                if (amount <= current_amount) and (amount > 0):
                    gadget[indeks][3] = current_amount - amount
                    print(f"Item {gadget[indeks][1]} (x{amount}) berhasil dipinjam!")
                    print()
                    terms = False
                else:
                    print(f"Jumlah yang anda ingin pinjam melebihi yang ada dalam stok penyimpanan atau anda memasukan angka di bawah 1. Silahkan masukan kembali jumlah yang ingin dipinjam dengan maksimal meminjam {current_amount}")
            except ValueError:
                print("Silahkan masukan kembali jumlah dengan angka yang benar")
    
        # Memasukan ke data gadget_borrow_history
        id_peminjaman = 'GBH' + str(len(gadget_borrow_history))
    
        gadget_borrow_history.append([id_peminjaman, idUser, id_item, date_string, amount, False])
    # Kondisi jika user pernah meminjam gadget dengan id = id_item, namun belum mengembalikannya
    else:
        print("Maaf, anda pernah meminjam gadget yang sama dan belum mengembalikannya, anda harus mengembalikan secara keseluruhan gadget yang baru saja anda ingin pinjam")
        print()