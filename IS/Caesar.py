def encrypt(plaintxt, shift):
    cipher = ""
    base = ord('A')
    for letter in plaintxt:
        cipher += chr((ord(letter) - base + shift ) % 26 + base)
    return cipher

def decrypt(ciphertxt, shift):
    plaintxt = ""
    base = ord('A')
    for letter in ciphertxt:
        plaintxt += chr((ord(letter) - base - shift + 26)%26 + base)
    return plaintxt

# plaintext = "hell0 world".upper().replace(" ", "")
plaintext = input("Enter plain text : ").upper().replace(" ", "")
shift = 3
cipher = encrypt(plaintext, shift)
print(cipher)

plaintext = decrypt(cipher, shift)
print(plaintext)
