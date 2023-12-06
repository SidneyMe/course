import random
import hashlib
from sympy import randprime, primitive_root

# Велике просте число
p = randprime(2**2048, 2**4096)
# Примітивний корінь по модулю p
g = primitive_root(p)

# Функція для обчислення НСД
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Генерація ключів
def generate_keys(p, g):
    a = random.randint(2, p)
    b = pow(g, a, p)
    return a, b

# Цифровий підпис
def sign(p, g, a, m):
    k = random.randint(2, p)
    while gcd(k, p - 1) != 1:
        k = random.randint(2, p)
    r = pow(g, k, p)
    Hm = int(hashlib.sha256(m.encode('utf-8')).hexdigest(), 16)
    s = ((Hm - a * r) * pow(k, -1, p-1)) % (p - 1)
    return r, s

# Перевірка підпису
def verify(p, g, b, m, r, s):
    try:
        Hm = int(hashlib.sha256(m.encode('utf-8')).hexdigest(), 16)
        y = pow(b, -1, p)
        u1 = (Hm * pow(s, -1, p-1)) % (p - 1)
        u2 = (r * pow(s, -1, p-1)) % (p - 1)
        v = (pow(g, u1, p) * pow(y, u2, p)) % p
        return v == r
    except ValueError:
        return False

# Зашифрування
def encrypt(p, g, b, m):
    k = random.randint(2, p)
    x = pow(g, k, p)
    y = (m * pow(b, k, p)) % p
    return x, y

# Розшифрування
def decrypt(p, a, x, y):
    s = pow(x, a, p)
    m = (y * pow(s, -1, p)) % p
    return m

def main():
    # Генерація ключів
    a, b = generate_keys(p, g)

    # Повідомлення
    m = "Hello, world!"

    # Підписання повідомлення
    r, s = sign(p, g, a, m)

    # Перевірка підпису
    print("Перевірка підпису: ", verify(p, g, b, m, r, s))

    # Зашифрування повідомлення
    x, y = encrypt(p, g, b, ord(m[0]))

    # Розшифрування повідомлення
    print("Розшифрування повідомлення: ", chr(decrypt(p, a, x, y)) == m[0])

if __name__ == '__main__':
    main()