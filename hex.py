#! /usr/bin/python

binaryHex ={
        "0": "0000","1": "0001","2": "0010","3": "0011",
        "4": "0100","5": "0101","6": "0110","7": "0111",
        "8": "1000","9": "1001","A": "1010","B": "1011",
        "C": "1100","D": "1101","E": "1110","F": "1111"
        }

def hexToBin( value ):
    value = value.upper()
    result = []
    for i in value:
        result.append(binaryHex[i])
    return ''.join(result)

print(hexToBin("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))

#    x = int(hex, 16)
#    return bin(x);

