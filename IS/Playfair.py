import random   

def getBogusChar(char):
    random_char = 'X'
    while random_char == char: 
        random_val = random.randint(65, 90) 
        random_char = chr(random_val)
    if random_char == 'J': 
        random_char = 'I'
    return random_char

def generate_key_table(keyword, alphabet):
    key_letters = []
    for char in keyword:
        if char not in key_letters:
            key_letters.append(char)

    complementary_elements = []
    for char in key_letters:
        if char not in complementary_elements:
            complementary_elements.append(char)
    for char in alphabet:
        if char not in complementary_elements:
            complementary_elements.append(char)

    matrix = []
    while complementary_elements:
        matrix.append(complementary_elements[:5])
        complementary_elements = complementary_elements[5:]

    return matrix

def search_position(element, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == element:
                return i, j
    return 0, 0

def encryptPlayFair(key, plaintext):
    ciphertext = ""
    plaintext = plaintext.replace('J', 'I') #J & I occupy same position in key grid
    for i in range(len(plaintext) - 1):
        if plaintext[i] == plaintext[i+1]:
            plaintext = plaintext[:i+1] + getBogusChar(plaintext[i]) + plaintext[i+1:]
 
    #ensure even no. of characters for generating pairs
    if len(plaintext) % 2 != 0:
        plaintext += getBogusChar(plaintext[-1]) 
    # print(plaintext)

    for i in range(0, len(plaintext)-1, 2):
        # locate pair's row and column
        row1, column1 = search_position(plaintext[i], key) 
        row2, column2 = search_position(plaintext[i+1], key)
        if (row1 == row2): # same row -> immediate right
            ciphertext += key[row1][(column1+1)%5]
            ciphertext += key[row1][(column2 + 1)%5]
        elif (column1 == column2): # same column -> immediate below
            ciphertext += key[(row1+1)%5][column1]
            ciphertext += key[(row2+1)%5][column1]
        else: # neither same row nor same column -> same row , match with other's column
            ciphertext += key[row1][column2]
            ciphertext += key[row2][column1]
    return ciphertext

text_plain = 'hello'.replace(" ", '').upper()
print("Plain Text:", text_plain)

keyword = "Monarchy".upper()
print("Key text:", keyword)

playfair_matrix = generate_key_table(keyword, 'ABCDEFGHIKLMNOPQRSTUVWXYZ') # exclude j

cipher_text = encryptPlayFair(playfair_matrix, text_plain)

print("CipherText:", cipher_text)
