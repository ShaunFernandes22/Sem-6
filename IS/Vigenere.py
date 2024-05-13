def encrypt(plaintxt, key):
    cipher = ""
    for i in range(len(plaintxt)):
        cipher += chr((ord(plaintxt[i]) + ord(key[i]))%26 + 65)
    return cipher

def decrypt(ciphertxt, key):
    plaintxt = ""
    for i in range(len(ciphertxt)):
        plaintxt += chr((ord(ciphertxt[i]) - ord(key[i]) +26)%26 +65)
    return plaintxt
    
def generateKey(plaintxt, key):
    if len(key) >= len(plaintext):
        return key

    new_key = list(key)
    excess = len(plaintxt) - len(key)
    k_len = len(key)
    for i in range(excess):
        new_key.append(key[i % k_len])

    return "".join(new_key)

# plaintext = "universal".upper()
plaintext = input("Enter plain text : ").upper().replace(" ", '')
# key = "college".upper()
key = input("Enter key : ").upper().replace(" ", '')

key = generateKey(plaintext, key)
cipher = encrypt(plaintext, key)
print(cipher)
plain = decrypt(cipher, key)
print(plain)
