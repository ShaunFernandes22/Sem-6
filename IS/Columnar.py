import math
def get_rank(key):
    rank = 1
    for char in sorted(key):
        key = key.replace(char, str(rank), 1)
        rank += 1
    key = [int(i) for i in key]
    return key

def encrypt(plaintxt, key):
    cols = len(key)
    rows = math.ceil(len(plaintxt)/cols)
    key_rank = get_rank(key)

    excess = rows * cols - len(plaintxt)
    for _ in range(excess):
        plaintxt += '_'
    
    matrix = [list(plaintxt[i : i+cols]) for i in range(0, len(plaintxt), cols)]
    for i in range(rows):
        print(matrix[i])

    cipher = ""
    for i in range(len(key_rank)):
        col_ind = key_rank.index(i+1)
        for row in range(rows):
            cipher += matrix[row][col_ind]

    return cipher

def decrypt(ciphertxt, key):
    cols = len(key)
    rows = math.ceil(len(ciphertxt)/cols)
    key_rank = get_rank(key)

    excess = rows*cols - len(ciphertxt)
    for i in range(excess):
        ciphertxt += '_'
    
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    ind_ct = 0

    plaintxt = ""
    for i in range(len(key_rank)):
        col_ind = key_rank.index(i+1)
        for row in range(rows):
            matrix[row][col_ind] = ciphertxt[ind_ct]
            ind_ct += 1

    for i in range(rows):
        for j in range(cols):
            plaintxt += matrix[i][j]

    plaintxt = plaintxt.rstrip('_')
    return plaintxt

plaintxt = "WEAREDISCOVEREDFLEEATONCE"
key1 = "ZEBRAS"
key2 = "STRIPE"

# plaintxt = "SPARTANSARECOMINGHIDEYOURWIFEANDKIDS"
# key1 = "POTATO"
# key2 = "SPARTA"

cipher = encrypt(plaintxt, key1)
print(cipher)

plaintxt = decrypt(cipher, key1)
print(plaintxt)

double_cipher = encrypt(cipher, key2)
d_decrypt = decrypt(decrypt(double_cipher,key2),  key1)
print(double_cipher)
print(d_decrypt)
