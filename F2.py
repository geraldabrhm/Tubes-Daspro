# ============================ F2 ========================================
def login():
    # Melakukan prosedur login ke program dengan mengecek apakah data yang diinputkan
    # sudah terdaftar di database
    
    # input ->  user : array of array of string and integer, 
    #           hasLogin, isAdmin : boolean 
    #           idUser : string
    # output -> hasLogin, isAdmin : boolean
    
    # I.S.  matriks data user, variable hasLogin, isAdmin, dan idUser terdefinisi
    # F.S.  mengubah variable hasLogin jika username dan password sesuai dengan data
    #       dan isAdmin jika rolenya adalah admin
    
    # KAMUS LOKAL
    # username, password : string
    # i : integer
    # rolling : boolean
    
    # Variable global
    global hasLogin
    global isAdmin
    global idUser
    
    # Function / Procedure
    # hashing(password : string) -> integer
    # Meng-hash password user menggunakan metode Polynomial Rolling Hash
    # I.S. password yang belum di hash terdefinisi
    # F.S. password ter-hash
    
    # Bold(text : string) -> string
    # Mengubah text menjadi terlihat bold jika di-print
    # I.S. text terdefinisi
    # F.S. text diberi 'kode' yang jika di-print text menjadi terlihat bold
    
    # ALGORITMA
    rolling = True
    while rolling:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
        for i in range(len(user)):
            # Mengecek apakah data yang diinputkan telah terdaftar di database
            if (username == user[i][1]) and (str(hashing(password)) == str(user[i][4])):
                hasLogin = True
                idUser = user[i][0]
                print("Selamat datang " + Bold(user[i][2]) + " ^_^")
                
                # Mengecek apakah rolenya Admin
                if user[i][5] == "Admin":
                    isAdmin = True
                break
        if not hasLogin:
            print("Username atau password Anda tidak cocok")
            print("Silakan masukkan kembali username dan password")
            print()
        else:
            rolling = False
    # rolling == False