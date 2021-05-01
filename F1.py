# ============================ F1 ========================================
def register():
    # Menambahkan data user baru ke dalam database
    
    # input/output -> user : array of array of string and integer 
    # I.S. matriks data user terdefinisi
    # F.S. matriks data user ditambahkan data user baru
    
    # KAMUS LOKAL
    # nama, username, password, alamat, idUser : string
    # notUnik : boolean
    # i, count : integer
    # register : array of array of string
    
    # Variable global
    global user 
    
    # Function / Procedure
    # hashing(password : string) -> integer
    # Meng-hash password user menggunakan metode Polynomial Rolling Hash
    # I.S. password yang belum di hash terdefinisi
    # F.S. password ter-hash
    
    # ALGORITMA
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    
    # Validasi username unik
    notUnik = True
    while notUnik:
        notUnik = False
        for i in range(len(user)):
            if user[i][1] == username:
                notUnik = True
                print()
                print("Username telah digunakan oleh user lain")
                print("Silakan input username yang berbeda")
                print()
                username = input("Masukkan username: ")
    # notUnik == False
    
    password = input("Masukkan password: ")
    alamat = input("Masukkan alamat: ")
    
    # Pembuatan idUSer
    count = 0
    for i in range(len(user)):
        if user[i][0][0] == 'U':
            count += 1
    id_user = "U" + str(count + 1)
    
    # Menambahkan data user baru ke dalam matriks data user
    register = [[id_user,username,nama,alamat,hashing(password),"User"]]
    user += register
    
    print("User", username, "telah berhasil register ke dalam Kantong Ajaib.")