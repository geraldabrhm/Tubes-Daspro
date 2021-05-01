def exit():
    # Menutup dan keluar dari program
    
    # input/output : -
    
    # I.S. program sedang berjalan
    # F.S. program ditutup dan selesai
    
    # KAMUS LOKAL
    # isSave : string
    
    # global variable
    global program
    
    # Function / Procedure
    # validasiYN(jawaban : string) -> boolean
    # Memvalidasi input dari user, harus 'Y' atau 'N'
    # I.S. string terdefinisi
    # F.S. mengembalikan True jika string adalah 'Y' atau 'N' dan False jika sebaliknya
    
    # ALGORITMA
    isSave = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ")
    while not validasiYN(isSave):
        isSave = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ")
    if isSave == "Y":
        save()
    print()
    print("Terima kasih telah menggunakan kantong ajaib ^_^")
    # Menghentikan program
    program = False
