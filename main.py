import os; import sys; import math; import time; import argparse; import datetime
from F1 import register; from F2 import login; from F3 import cariRarity; from F4 import caritahun; from F5 import tambahItem; from F6 import hapusItem
from F7 import ubahjumlah; from F8 import pinjam; from F9nFB02 import kembalikan; from F10 import mintaConsumable; from F11 riwayatPinjam; from F12 import riwayatKembali
from F13 import riwayatConsumable; from F14 import load_data; from F15 import save_data; from F16 import help; from F17 import exit; 
from FB01 import hashing; from FB02 import seed; from FB03 import; from FTambahan import Bold, modify_data, cariID, IDItemAda, cariData, colorStr, tglValid, validasiYN, 

# ============================== MAIN PROGRAM =======================================

user =[]; gadget = []; consumable = []; consumable_history = []; gadget_borrow_history = []; gadget_return_history = []; inventory_user = []
idUser = ""; random=0; lstChance = [0,0,0,0]
lstPerintah = ['register', 'login', 'caricarity', 'caritahun', 'tambahitem', 'hapusitem', 'ubahjumlah', 'pinjam', 
               'kembalikan', 'minta', 'riwayatpinjam', 'riwayatkembali', 'riwayatambil', 'save', 'help', 'gacha']


program = True
hasLogin = False
isAdmin = False

directory = loading()

if not(directory == None):
    print("Loading...")
    time.sleep(2)
    load(directory)
    print()
    print("""\
\033[93m __  __               __                          _______ __         __ __    \033[0m
\033[93m|  |/  |.---.-.-----.|  |_.-----.-----.-----.    |   _   |__|.---.-.|__|  |--.\033[0m
\033[93m|     < |  _  |     ||   _|  _  |     |  _  |    |       |  ||  _  ||  |  _  |\033[0m
\033[93m|__|\__||___._|__|__||____|_____|__|__|___  |    |___|___|  ||___._||__|_____|\033[0m
\033[93m                                      |_____|           |___|                 \033[0m
\033[36m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣶⣶⣶⠶⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀ \033[0m
\033[36m⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⠁⠀⢀⠈⢿⢀⣀⠀⠹⣿⣿⣿⣦⣄⠀⠀⠀ \033[0m
\033[36m⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⠿⠀⠀⣟⡇⢘⣾⣽⠀⠀⡏⠉⠙⢛⣿⣷⡖⠀ \033[0m
\033[36m⠀⠀⠀⠀⠀⣾⣿⣿⡿⠿⠷⠶⠤⠙⠒⠀⠒⢻⣿⣿⡷⠋⠀⠴⠞⠋⠁⢙⣿⣄ \033[0m
\033[36m⠀⠀⠀⠀⢸⣿⣿⣯⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠉⢹⡄⠀⠀⠀⠛⠛⠋⠉⠹⡇ \033[0m
\033[36m⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣼⣇⣀⣀⣀⣛⣛⣒⣲⢾⡷ \033[0m
\033[36m⢀⠤⠒⠒⢼⣿⣿⠶⠞⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣼⠃ \033[0m
\033[36m⢮⠀⠀⠀⠀⣿⣿⣆⠀⠀⠻⣿⡿⠛⠉⠉⠁⠀⠉⠉⠛⠿⣿⣿⠟⠁⠀⣼⠃⠀ \033[0m
\033[36m⠈⠓⠶⣶⣾⣿⣿⣿⣧⡀⠀⠈⠒⢤⣀⣀⡀⠀⠀⣀⣀⡠⠚⠁⠀⢀⡼⠃⠀⠀ \033[0m
\033[36m⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣭⣭⣭⣭⣭⣥⣤⣤⣤⣴⣟⠁\033[0m
                        """)
    print('Selamat datang di "Kantong Ajaib!"')

    while (program):
        print(colorStr(">>> ","red"),end='')
        perintah = input()
        if perintah == "help":
            help()
        elif perintah == "login":
            if hasLogin:
                print(colorStr("Anda sudah login, exit terlebih dahulu untuk menggunakan akun lain","red"))
                print()
            else:
                login()
        elif perintah == "exit":
            exit()
            print("""\
                
\033[36m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣶⣶⣶⠶⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀ \033[0m
\033[36m⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⠁⠀⢀⠈⢿⢀⣀⠀⠹⣿⣿⣿⣦⣄⠀⠀⠀ \033[0m
\033[36m⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⠿⠀⠀⣟⡇⢘⣾⣽⠀⠀⡏⠉⠙⢛⣿⣷⡖⠀ \033[0m
\033[36m⠀⠀⠀⠀⠀⣾⣿⣿⡿⠿⠷⠶⠤⠙⠒⠀⠒⢻⣿⣿⡷⠋⠀⠴⠞⠋⠁⢙⣿⣄ \033[0m
\033[36m⠀⠀⠀⠀⢸⣿⣿⣯⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠉⢹⡄⠀⠀⠀⠛⠛⠋⠉⠹⡇ \033[0m
\033[36m⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣼⣇⣀⣀⣀⣛⣛⣒⣲⢾⡷ \033[0m
\033[36m⢀⠤⠒⠒⢼⣿⣿⠶⠞⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣼⠃ \033[0m
\033[36m⢮⠀⠀⠀⠀⣿⣿⣆⠀⠀⠻⣿⡿⠛⠉⠉⠁⠀⠉⠉⠛⠿⣿⣿⠟⠁⠀⣼⠃⠀ \033[0m
\033[36m⠈⠓⠶⣶⣾⣿⣿⣿⣧⡀⠀⠈⠒⢤⣀⣀⡀⠀⠀⣀⣀⡠⠚⠁⠀⢀⡼⠃⠀⠀ \033[0m
\033[36m⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣭⣭⣭⣭⣭⣥⣤⣤⣤⣴⣟⠁\033[0m
                                """)
        else:
            if hasLogin:
                if perintah == "register":
                    if isAdmin:
                        register()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "carirarity":
                    cariRarity()
                elif perintah == "caritahun":
                    caritahun()
                elif perintah == "tambahitem":
                    if isAdmin:
                        tambahItem()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "hapusitem":
                    if isAdmin:
                        hapusItem()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "ubahjumlah":
                    if isAdmin:
                        ubahjumlah()
                    else:    
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "pinjam":
                    if not isAdmin:
                        pinjam()
                    else:
                        print("Maaf, hanya boleh diakses oleh user ^_^")
                        print()
                elif perintah == "kembalikan":
                    if not isAdmin:
                        kembalikan()
                    else:
                        print("Maaf, hanya boleh diakses oleh user ^_^")
                        print()
                elif perintah == "minta":
                    if not isAdmin:
                        mintaConsumable()
                    else:
                        print("Maaf, hanya boleh diakses oleh user ^_^")
                        print()
                elif perintah == "riwayatpinjam":
                    if isAdmin:
                        riwayatPinjam()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "riwayatkembali":
                    if isAdmin:    
                        riwayatKembali()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "riwayatambil":
                    if isAdmin:
                        riwayatConsumable()
                    else:
                        print("Maaf, hanya boleh diakses oleh admin ^_^")
                        print()
                elif perintah == "save":
                    save()

                elif perintah == "gacha":
                    gacha()
                else:
                    print(colorStr("Input anda tidak valid, ketik help untuk mendapatkan daftar input yang valid","red"))
                    print("Berikut merupakan input yang valid")
                    help()        
            elif perintah in lstPerintah:
                print(colorStr("Anda harus login terlebih dahulu","red"))
                print()
            else:
                print(colorStr("Input yang diberikan tidak tersedia","red"))
                print()
