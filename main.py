import hashlib 
import itertools 
import string 

def find_string(*args):
    hash_value, lenght = args
    characters = string.ascii_letters + string.digits # alphabet creator "AaBbCc.." +  "123.."
    for attempt in itertools.product(characters, repeat=lenght): # going through all possible strs
        attempt = ''.join(attempt)
        # print(attempt) if you want watch a mess )
        sha3_hash = hashlib.sha3_256(attempt.encode()).hexdigest() # encode attempted str
        # print(sha3_hash)
        if sha3_hash == hash_value:
            return attempt
    return None

def main():
    hash_values = [
        'a03ab19b866fc585b5cb1812a2f63ca861e7e7643ee5d43fd7106b623725fd67',
        'd182aed568b01fee105557a1d173791c798030db267cf94e17102b94dcbbda3c',
        '7b6a784b05c64d2e669e026fc61296eca2ee8acd5112eb8ae5f16023809e203b'
    ]

    for hash_value in hash_values:
        print(f'Finding string for hash: {hash_value}')
        for length in range(1, 7): # < correct length here
            result = find_string (hash_value, length)
            if result is not None:
                print(f'Found string: {result}')
                break
        else :
            print('No string found')

if __name__ == '__main__':
    main()