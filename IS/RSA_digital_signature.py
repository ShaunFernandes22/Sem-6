import hashlib
import random

def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def find_e(phi):
    e = 2
    while e < phi:
        if gcd(phi, e) == 1:
            break
        e += 1
    return e

def find_d(e, phi):
    return pow(e, -1, phi)

def generate_keys():
    p = random.randint(1, 200)
    q = random.randint(1, 200)
    while not isPrime(p):
        p = random.randint(1, 200)
    while not isPrime(q):
        q = random.randint(1, 200)
    n = p * q
    phi = (p-1) * (q-1)
    e = find_e(phi)
    d = find_d(e, phi)

    return (e, n), (d, n), n

def encrypt(msg, private_key):
    d, n = private_key
    cipher = pow(msg, d, n)
    return cipher 

def decrypt(msg, public_key):
    e, n = public_key
    plaintxt = pow(msg, e, n)
    return plaintxt

public_key, private_key, n = generate_keys()
message = "This is Agent Binod"
message_hash = int(hashlib.md5(message.encode()).hexdigest(), 16)%n

signature = encrypt(message_hash, private_key)

hash_from_certificate = decrypt(signature, public_key)

if message_hash == hash_from_certificate:
    print("Verified")
else:
    print("No")
