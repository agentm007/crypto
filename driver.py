#!/usr/bin/python
import cusbase64
import cushex
import cusbitops

#v1 = cushex.hexToBin(value)

#Set 1 Challenge 1
#testhex='FF'
#print cushex.hexToBin(testhex)
#test64='010011010110000101101110'
#print cusbase64.binToBase64(test64)
#value = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
#answer = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
#value = cushex.hexToBin(value)
#value = cusbase64.binToBase64(value)
#if(value == answer):
#    print("Correct")

#Set 1 Challenge 2
test1 = '1111'
test2 = '1'
print(cusbitops.xor(test1,test2))
value1 = '1c0111001f010100061a024b53535009181c'
value2 = '686974207468652062756c6c277320657965'
answer = '746865206b696420646f6e277420706c6179'
xored = cusbitops.xor(cushex.hexToBin(value1),cushex.hexToBin(value2))
xored = cushex.binToHex(xored)
answer = answer.upper()
if(xored == answer):
    print("Correct")
