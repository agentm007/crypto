#!/usr/bin/python

def xor(value1, value2):
    result = []
    length = len(value1)
    lv2 = len(value2)
    if( length == lv2 ):
        for i in range(length):
            if((value1[i] == '1' or value2[i] == '1') and value1[i] != value2[i]):
                result.append('1')
            else:
                result.append('0')
    else:
        lneeded = length - lv2
        mult = lneeded/lv2
        value2 = value2 * (mult+1)
        for i in range(length):
            if((value1[i] == '1' or value2[i] == '1') and value1[i] != value2[i]):
                result.append('1')
            else:
                result.append('0')
    return ''.join(result)
