import time
import hashlib
import random
import string

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

def sha1(data):
    bytes = ""

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    for n in range(len(data)):
        bytes += '{0:08b}'.format(ord(data[n]))
    bits = bytes+"1"
    pBits = bits
    while len(pBits)%512 != 448:
        pBits += "0"
    pBits += '{0:064b}'.format(len(bits)-1)

    for c in range(len(pBits)//512): 
        chunk = pBits[c*512:(c+1)*512]
        words = []
        for i in range(16):
            words.append(int(chunk[i*32:(i+1)*32], 2))
        for i in range(16, 80):
            words.append(left_rotate((words[i-3] ^ words[i-8] ^ words[i-14] ^ words[i-16]), 1) & 0xffffffff)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d) 
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = left_rotate(a, 5) + f + e + k + words[i] & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

def generate_random_word(min_length=3, max_length=100):
    arr = []
    for _ in range(1000): 
        length = random.randint(min_length, max_length)
        letters = string.ascii_lowercase
        arr += [''.join(random.choice(letters) for _ in range(length))]
    return arr

@timer_decorator
def my_sha1(words):
    hashes = []
    for word in words:
        hashes.append(sha1(word))
    return hashes
    
@timer_decorator
def thirdparty_sha1(words):
    hashes = []
    for word in words:
        hashes.append(hashlib.sha1(word.encode()).hexdigest())
    return hashes

def main():
    words = generate_random_word()
    my_hashes = my_sha1(words)
    thirdparty_hashes = thirdparty_sha1(words)
    for i in range(len(my_hashes)):
        if my_hashes[i] == thirdparty_hashes[i]:
            print(f"Hashes for word {i+1} are similar.")
    
if __name__ == '__main__':
    main()