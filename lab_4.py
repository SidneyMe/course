import random
import itertools
from collections import Counter

# Генерує випадкову послідовність бітів заданої довжини
def generate_random_sequence(n_bits=20000):
    return [random.randint(0, 1) for _ in range(n_bits)]

# Монобітний тест: перевіряє, чи є кількість біт "0" і "1" приблизно однаковою
def monobit_test(bits):
    count = sum(bits)
    return 9654 < count < 10346

# Тест на максимальну довжину серії: перевіряє, чи не перевищує найбільша послідовність однакових біт 36
def longest_run_test(bits):
    groups = (list(g) for _, g in itertools.groupby(bits))
    max_run = max(len(g) for g in groups)
    return max_run <= 36

# Тест Покера: перевіряє розподіл 4-бітних блоків у послідовності
def poker_test(bits, m=4):
    k = len(bits) // m
    blocks = [''.join(map(str,bits[i*m:(i+1)*m])) for i in range(k)]
    counts = Counter(blocks).values()
    x3 = (2**m/k) * sum(c**2 for c in counts) - k
    return 1.03 < x3 < 57.4

# Тест на довжини серій: перевіряє кількость пробігу однакових біт розміру 1-6
def runs_test(bits):
    bit_values = [0, 1]
    max_len = 6
    intervals = [(2267, 2733), (1079, 1421), (502, 748), (223, 402), (90, 223), (90, 223)]
    
    for bit in bit_values:
        runs = [len(list(g)) for k, g in itertools.groupby(bits) if k == bit]
        counts = [runs.count(i) for i in range(1, max_len+1)]
        counts.append(sum(1 for i in runs if i >= max_len+1))
        
        for i in range(max_len):
            if not intervals[i][0] <= counts[i] <= intervals[i][1]:
                return False
            
    return True

# Виконує всі чотири тести FIPS-140 на вхідну послідовність біт
def fips_140_test(bits):
    tests = [monobit_test, longest_run_test, poker_test, runs_test]
    results = [test(bits) for test in tests]
    return all(results)

# Головна функція: генерує 1000 випадкових послідовностей бит і перевіряє, сколько з них проходять тести FIPS-140
def main():
    rolls = 1000
    real_rand = 0
    for _ in range(rolls):
        bits = generate_random_sequence()
        if fips_140_test(bits) == True:
             real_rand += 1
    print(f'Кількість наборів данних які відповіли усім умовам {real_rand} з {rolls} згенерованих')

if __name__ == '__main__':
    main()
