import random

def left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def H(b, c, d):
    return b ^ c ^ d

def simple_md5(message):
    og_msg_len = len(message)
    message += "1"
    padding_length = 512 - ((len(message) + 64) % 512)
    message += "0" * padding_length

    msg_len = f"{og_msg_len:064b}"
    message += msg_len

    message_words = [int(message[i: i+32], 2) for i in range(0, len(message), 16)]
    A, B, C, D = [0x01234567, 0x89ABCDEF, 0xFEDCBA98, 0x76543210]
    key = 0x1357ACDF

   
    a, b, c, d = A, B, C, D
    
    #just 4 * 32 bits
    func = H(b, c, d)
    a = (a + func + message_words[0]) & 0xFFFFFFFF
    a = (a + key) & 0xFFFFFFFF
    a = left_rotate(a, 5)
    a = (a+b) & 0xFFFFFFFF
    a, b, c, d = b, c, d, a

    return f"{a:08x}{b:08x}{c:08x}{d:08x}"

message = "".join([random.choice(["0", "1"]) for _ in range(1000)])
hash = simple_md5(message)
print(hash)
