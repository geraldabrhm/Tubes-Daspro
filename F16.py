# ============================ F16 ========================================
def help():
    # Menampilkan keyword-keyword yang tersedia ke layar
    
    # input/output : -
    
    # I.S. sembarang
    # F.S. tercetak list keyword ke layar
    
    # KAMUS LOKAL
    # -
    
    # Function / Procedure
    # -
    
    # ALGORITMA
    
    print("""
============================================================ HELP ============================================================
Berikut merupakan keyword yang dapat digunakan beserta fungsi dan aksesnya
Ketikkan keyword di bawah ini untuk melakukan fungsi yang diinginkan
> \033[1mregister\033[0m       => melakukan registrasi user baru                                                  \033[91m(Akses: Admin)\033[0m
> \033[1mlogin\033[0m          => melakukan login ke dalam program                                                \033[91m(Akses: Admin/User)\033[0m
> \033[1mcaricarity\033[0m     => mencari gadget berdasarkan rarity yang diinputkan                               \033[91m(Akses: Admin/User)\033[0m
> \033[1mcaritahun\033[0m      => mencari gadget berdasarkan tahun ditemukan                                      \033[91m(Akses: Admin/User)\033[0m
> \033[1mtambahitem\033[0m     => menambahkan item (gadget/consumable) ke dalam database                          \033[91m(Akses: Admin)\033[0m
> \033[1mhapusitem\033[0m      => menghapus item (gadget/consumable) dari database                                \033[91m(Akses: Admin)\033[0m
> \033[1mubahjumlah\033[0m     => mengubah jumlah gadget/consumable pada database                                 \033[91m(Akses: Admin)\033[0m
> \033[1mpinjam\033[0m         => meminjam gadget dari database dan memasukkan ke dalam inventory                 \033[91m(Akses: User)\033[0m
> \033[1mkembalikan\033[0m     => mengembalikan gadget yang dipinjam                                              \033[91m(Akses: User)\033[0m
> \033[1mminta\033[0m          => meminta consumable dari database dan memasukkan ke dalam inventory              \033[91m(Akses: User)\033[0m
> \033[1mriwayatpinjam\033[0m  => melihat record peminjaman gadget yang tersortir berdasar tanggal                \033[91m(Akses: Admin)\033[0m
> \033[1mriwayatkembali\033[0m => melihat record pengembalian gadget yang tersortir berdasar tanggal              \033[91m(Akses: Admin)\033[0m
> \033[1mriwayatambil\033[0m   => melihat record pengambilan consumable yang tersortir berdasar tanggal           \033[91m(Akses: Admin)\033[0m
> \033[1msave\033[0m           => menyimpan data setelah dilakukan perubahan                                      \033[91m(Akses: Admin/User)\033[0m
> \033[1mhelp\033[0m           => memberikan panduan penggunaan sistem                                            \033[91m(Akses: Admin/User)\033[0m
> \033[1mgacha\033[0m          => menggacha consumable yang ada di inventory untuk mendapatkan consumable baru    \033[91m(Akses: User)\033[0m
> \033[1mexit\033[0m           => keluar dari program                                                             \033[91m(Akses: Admin/User)\033[0m
          """)