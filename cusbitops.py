#!/usr/bin/python
import math


def xor(value1, value2):
    result = []
    length = len(value1)
    lv2 = len(value2)

    if(not(length <= lv2)):
        lneeded = length - lv2
        mult = math.ceil(lneeded/lv2)
        value2 += value2 * int(mult)

    for i in range(length):
        if((value1[i] == '1' or value2[i] == '1') and (value1[i] != value2[i])):
            result.append('1')
        else:
            result.append('0')
    return ''.join(result)

def binToASCII(value):
    result = []
    length = len(value)
    for i in range(0, length, 8):
        combine = int(value[i:i+8], 2)
        if(combine <= 128):
            result.append(str(unichr(combine)))
        else:
            result.append(' ')
    return ''.join(result)

def ASCIITobin(value):
    result = []
    length = len(value)
    for i in range(0, length):
        
