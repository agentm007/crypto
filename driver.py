#!/usr/bin/python
import cusbase64
import cushex
import cusbitops
import analyze
import string

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

##Set 1 Challenge 2
##xor test
#testxor1 = '1111'
#testxor2 = '1'
#print(cusbitops.xor(testxor1,testxor2))
##binToHex test
#testhex1 = ''
#testhex2 = ''
#
#value1 = '1c0111001f010100061a024b53535009181c'
#value2 = '686974207468652062756c6c277320657965'
#answer = '746865206b696420646f6e277420706c6179'
#xored = cusbitops.xor(cushex.hexToBin(value1),cushex.hexToBin(value2))
#xored = cushex.binToHex(xored)
#answer = answer.upper()
#if(xored == answer):
#    print("Correct")


#Set 1 Challenge 3
value = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#print analyze.charfreq('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#print analyze.charfreq('test')
#print analyze.charfreq('The first thing to know about me is that I dont judge people unfairly')
#print analyze.charfreq('fasoyenuvenfggjdiudeneuekkvdfa;ksfjvneimkllajflsfjaskluveioqnpeopqru')
#print analyze.charfreq('the quick brown fox jumped over the lazy dog')
#print analyze.charfreq("In my younger and more vulnerable years my father gave me some advice that Ive been turning over in my mind ever since. Whenever you feel like criticizing any one he told me just remember that all the people in this world havent had the advantages that youve had.")
#
#Testing ASCIITobin method
print cusbitops.ASCIITobin('A')

binvalue = cushex.hexToBin(value)
for i in string.ascii_letters:
    print analyze.charfreq(cusbitops.binToASCII(cusbitops.xor(cushex.hexToBin(value),cusbitops.ASCIITobin(i))))
