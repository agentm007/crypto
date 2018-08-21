#!/usr/bin/python
import cusbitops

hexBinary ={
        "0": "0000","1": "0001","2": "0010","3": "0011",
        "4": "0100","5": "0101","6": "0110","7": "0111",
        "8": "1000","9": "1001","A": "1010","B": "1011",
        "C": "1100","D": "1101","E": "1110","F": "1111"
        }
binaryHex = {
        "0000": "0","0001": "1","0010": "2","0011": "3",
        "0100": "4","0101": "5","0110": "6","0111": "7",
        "1000": "8","1001": "9","1010": "A","1011": "B",
        "1100": "C","1101": "D","1110": "E","1111": "F"
        }

def hexToBin(value):
    value = value.upper()
    result = []
    for i in value:
        result.append(hexBinary[i])
    return ''.join(result)

def binToHex(value):
    length = len(value)
    result = []
    for i in range(0, length, 4):
        result.append(binaryHex[value[i:i+4]])
    return ''.join(result)

def hexToASCII(value):
    return cusbitops.binToASCII(hexToBin(value))
