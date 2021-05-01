# ============================ FB01 ========================================
def hashing(str):
    # Melakukan hashing pada password dengan metode RollingHash yang bersifat satu arah
    
    # input -> str : string
    # output -> integer
    
    # I.S. string password terdefinisi
    # F.S. string password telah dilakukan hashing
    
    # KAMUS LOKAL
    # P, m, powerOfP, hashed, i : integer
    
    # Function / Procedure
    # -
    
    # ALGORITMA
    P = 101
    m = 1e9 + 1
    powerOfP = 1
    hashed = 0
    for i in range(len(str)):
        hashed = ((hashed + (ord(str[i]) - ord('!') + 1) * powerOfP) % m) 
        powerOfP = (powerOfP * P) % m
    return int(hashed)