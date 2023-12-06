import random

def is_prime(number):
    if number <= 1 or (number % 2 == 0 and number > 2): 
        return False
    return all(number % i for i in range(3, int(number**0.5) + 1, 2))

def find_coprime(a):
    b = random.randint(2, a-1)
    while True:
        if (b == 1) or (not is_prime(b)) or (a % b == 0):
            b = random.randint(2, a-1)
        else:
            return b

def calculate_mod_inverse(e, m):
    for i in range(1, m):
        if (e * i) % m == 1:
            return i
    return -1

def generate_keys():
    prime1, prime2 = 11, 13
    n = prime1 * prime2
    m = (prime1 - 1) * (prime2 - 1)
    e = find_coprime(m)
    d = calculate_mod_inverse(e, m)
    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

def main():
    public_key, private_key = generate_keys()
    message = 7
    ciphertext = encrypt(message, public_key)
    decrypted_message = decrypt(ciphertext, private_key)
    print(f"Original message: {message}")
    print(f"Encrypted message: {ciphertext}")
    print(f"Decrypted message: {decrypted_message}")

if __name__ == '__main__':
    main()