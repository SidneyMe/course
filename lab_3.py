class SBlock:
    S_BOX = [
        [3, 10, 8, 15, 0, 13, 6, 1, 14, 9, 7, 12, 11, 5, 2, 4],
        [15, 5, 2, 8, 1, 12, 14, 10, 7, 3, 13, 0, 6, 11, 9, 4],
        [1, 14, 7, 9, 0, 2, 13, 15, 6, 12, 10, 11, 8, 3, 5, 4],
        [13 ,6 ,0 ,9 ,10 ,1 ,15 ,2 ,14 ,7 ,5 ,8 ,3 ,12 ,11 ,4]
    ]


    def transform(input_bits):
        left_bits = input_bits[:4]
        right_bits = input_bits[4:]
        
        left_row = int(left_bits[0] + left_bits[3],2)
        left_col = int(left_bits[1] + left_bits[2],2)
        
        right_row = int(right_bits[0] + right_bits[3],2)
        right_col = int(right_bits[1] + right_bits[2],2)
        
        return format(SBlock.S_BOX[left_row][left_col], '04b') + format(SBlock.S_BOX[right_row][right_col], '04b')

    def inverse(output_bits):
        left_output_value = int(output_bits[:4] ,2)
        right_output_value = int(output_bits[4:] ,2)
        
        for row,row_values in enumerate(SBlock.S_BOX):
            if left_output_value in row_values:
                left_col = row_values.index(left_output_value)
                left_result = format(row,'02b') + format(left_col,'02b')
            if right_output_value in row_values:
                right_col = row_values.index(right_output_value)
                right_result = format(row,'02b') + format(right_col,'02b')
        
        return left_result + right_result

class PBlock:
    def transform(input_bits):
        permutation_order = [7, 2, 5, 1, 6, 0, 4, 3]
        return ''.join(input_bits[i] for i in permutation_order)

    def inverse(output_bits):
        permutation_order = [5, 3, 1, 7, 6, 2, 4, 0]
        return ''.join(output_bits[i] for i in permutation_order)
    
def main():
    test_data = ['10000001']
    
    print("Testing S-block:")
    for data in test_data:
        output_data = SBlock.transform(data)
        print(f'Input data: {data}, Output data: {output_data}')
    
    print("\nTesting P-block:")
    for data in test_data:
        output_data = PBlock.transform(data)
        print(f'Input data: {data}, Output data: {output_data}, Reverse transformation: {PBlock.inverse(output_data)}')

if  __name__ == '__main__':
    main()