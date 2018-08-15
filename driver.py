#!/usr/bin/python
import cusbase64
import cushex
import cusbitops

value = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#v1 = cushex.hexToBin(value)
v2 = cushex.hexToASCII(value)
print v2


#val = cusbitops.xor(v1, '1111')
#print(val)
#print(cushex.binToHex(val))

#for i in range(65, 91):


#print(cushex.binToHex(cushex.hexToBin('1c0111001f010100061a024b53535009181c')))
#print(cusbase64.binToBase64(cushex.hexToBin("41")))
