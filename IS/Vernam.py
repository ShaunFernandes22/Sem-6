def encrypt(plaintxt, key):
    result = ""
    for i in range(len(plaintxt)):
        value = (ord(plaintxt[i])-65) ^ (ord(key[i]) - 65) % 26
        result += chr(value + 65) 
    return result


plaintxt = "hello".upper()
key = "mango".upper()
cipher = encrypt(plaintxt, key)
print(cipher)
plain = encrypt(cipher, key)
print(plain)
