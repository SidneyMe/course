class BigNumber:  
    def __init__(self):
        self.data = []

    def setFromHexString(self, hexString):
        self.data = [int(hexString[i:i+8], 16) for i in range(0, len(hexString), 8)]

    def getAsHexString(self):
        return ''.join('{:08x}'.format(i) for i in self.data)

    def INV(self):
        self.data = [~i & 0xFFFFFFFF for i in self.data]

    def AND(self, other):
        self.data = [i & j for i, j in zip(self.data, other.data)]

    def OR(self, other):
        self.data = [i | j for i, j in zip(self.data, other.data)]

    def XOR(self, other):
        self.data = [i ^ j for i, j in zip(self.data, other.data)]

    def shiftR(self, n):
        self.data = [i >> n for i in self.data]

    def shiftL(self, n):
        self.data = [i << n for i in self.data]

    def ADD(self, other):
        carry = 0
        for i in range(len(self.data)):
            sum = self.data[i] + other.data[i] + carry
            self.data[i] = sum & 0xFFFFFFFF
            carry = sum >> 32
        if carry != 0:
            self.data.append(carry)

    def SUB(self, other):
        borrow = 0
        for i in range(len(self.data)):
            diff = self.data[i] - other.data[i] - borrow
            if diff < 0:
                diff += 1 << 32
                borrow = 1
            else:
                borrow = 0
            self.data[i] = diff
    
    def MOD(self, other):
        self_as_int = int(self.getAsHexString(), 16)
        other_as_int = int(other.getAsHexString(), 16)
        
        if other_as_int != 0:
            result_as_int = self_as_int % other_as_int
            self.setFromHexString(format(result_as_int, 'x'))
        else:
            raise ValueError("Division by zero")


def run_operation(bn1, bn2, hex1, hex2, operation, op_name):
    bn1.setFromHexString(hex1)
    bn2.setFromHexString(hex2)
    if operation == bn1.INV:
        operation()
    else:
        operation(bn2)
    print(f'{op_name} = {bn1.getAsHexString()}\n')


def run_tests():
    bn1 = BigNumber()
    bn2 = BigNumber()

    run_operation(bn1, bn2, "51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4",
                  "403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c", bn1.INV, 'INV')
    run_operation(bn1, bn2, "51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4",
                  "403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c", bn1.AND, 'AND')
    run_operation(bn1, bn2, "51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4",
                  "403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c", bn1.OR, 'OR')
    run_operation(bn1, bn2, "51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4",
                  "403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c", bn1.XOR, 'XOR')
    run_operation(bn1, bn2, "36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80",
                  "70983d692f648185febe6d6fa607630ae68649f7e6fc45b94680096c06e4fadb", lambda x: bn1.shiftL(5), 'ShiftL')
    run_operation(bn1, bn2, "51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4",
                  "403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c", lambda x: bn1.shiftR(5), 'ShiftR')
    run_operation(bn1, bn2, "36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80",
                  "70983d692f648185febe6d6fa607630ae68649f7e6fc45b94680096c06e4fadb", bn1.ADD, 'ADD')
    run_operation(bn1, bn2, "33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc",
                  "22e962951cb6cd2ce279ab0e2095825c141d48ef3ca9dabf253e38760b57fe03", bn1.SUB, 'SUB')
    run_operation(bn1, bn2, "33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc",
                  "403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c", bn1.MOD, 'MOD')

def main():
    run_tests()

if __name__ == '__main__':
    main()