from Crypto.PublicKey import ECC
import random

class ECPoint:
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve

def BasePointGGet(curve):
    key = ECC.generate(curve=curve)
    return ECPoint(key.pointQ.x, key.pointQ.y, key.curve)

def ECPointGen(curve):
    key = ECC.generate(curve=curve)
    x, y = key.pointQ.x, key.pointQ.y
    return ECPoint(x, y, curve)

def IsOnCurveCheck(a):
    point = ECC.EccPoint(a.x, a.y, a.curve)
    return point.is_valid()

def AddECPoints(a, b):
    point_a = ECC.EccPoint(a.x, a.y, a.curve)
    point_b = ECC.EccPoint(b.x, b.y, b.curve)
    result_point = point_a + point_b
    return ECPoint(result_point.x, result_point.y, a.curve)

def DoubleECPoints(a):
    point_a = ECC.EccPoint(a.x, a.y, a.curve)
    result_point = 2 * point_a
    return ECPoint(result_point.x, result_point.y, a.curve)

def ScalarMult(k, a):
    point_a = ECC.EccPoint(a.x, a.y, a.curve)
    result_point = k * point_a
    return ECPoint(result_point.x, result_point.y, a.curve)

def ECPointToString(point):
    return f'{point.x}, {point.y}'

def StringToECPoint(s):
    x, y = map(int, s[1:-1].split(', '))
    return ECPoint(x, y)

def PrintECPoint(point):
    print(f'({point.x}, {point.y})')

def main():
    curves = [
        'NIST P-192', 'p192', 'P-192', 'prime192v1', 'secp192r1',
        'NIST P-224', 'p224', 'P-224', 'prime224v1', 'secp224r1',
        'NIST P-256', 'p256', 'P-256', 'prime256v1', 'secp256r1',
        'NIST P-384', 'p384', 'P-384', 'prime384v1', 'secp384r1',
        'NIST P-521', 'p521', 'P-521', 'prime521v1', 'secp521r1',
        'ed25519', 'Ed25519', 
        'ed448', 'Ed448'
    ]

    k = random.getrandbits(256)
    d = random.getrandbits(256)
    
    for curve in curves:
        G = BasePointGGet(curve)
        random_point = ECPointGen(curve)

        H1 = ScalarMult(d, G)
        H2 = ScalarMult(k, H1)

        H3 = ScalarMult(k, G)
        H4 = ScalarMult(d, H3)

        result = (H2.x == H4.x) and (H2.y == H4.y)
        print(f'{curve}: {result}')

        print(f'Random Point on {curve}: {ECPointToString(random_point)}\n')

if __name__ == "__main__":
    main()
