#!/usr/bin/python
import cusbase64
import cushex
import cusbitops
import analyze
import string
import operator

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
#value = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#print analyze.charfreq('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#print analyze.charfreq('test')
#print analyze.charfreq('The first thing to know about me is that I dont judge people unfairly')
#print analyze.charfreq('fasoyenuvenfggjdiudeneuekkvdfa;ksfjvneimkllajflsfjaskluveioqnpeopqru')
#print analyze.charfreq('the quick brown fox jumped over the lazy dog')
#print analyze.charfreq("In my younger and more vulnerable years my father gave me some advice that Ive been turning over in my mind ever since. Whenever you feel like criticizing any one he told me just remember that all the people in this world havent had the advantages that youve had.")
#
#Testing ASCIITobin method
#print cusbitops.ASCIITobin('A')
#
##Breaking the encoding
#binvalue = cushex.hexToBin(value)
#final = []
#for i in string.ascii_letters:
#    letterbin = cusbitops.ASCIITobin(i)
#    letters = cusbitops.binToASCII(cusbitops.xor(binvalue,letterbin))
#    score = analyze.charfreq(letters)
#    transfer = [letterbin, letters, score]
#    final.append(transfer)
#final.sort(key=operator.itemgetter(2))
#
##Printing the top 10 results
#for i in range(0,10):
#    print final[i]


##Set 1 Challenge 4
##Wordsearch test
#print analyze.wordSearch('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#print analyze.wordSearch('test')
#print analyze.wordSearch('The first thing to know about me is that I dont judge people unfairly')
#print analyze.wordSearch('fasoyenuvenfggjdiudeneuekkvdfa;ksfjvneimkllajflsfjaskluveioqnpeopqru')
#print analyze.wordSearch('the quick brown fox jumped over the lazy dog')
#print analyze.wordSearch("In my younger and more vulnerable years my father gave me some advice that Ive been turning over in my mind ever since. Whenever you feel like criticizing any one he told me just remember that all the people in this world havent had the advantages that youve had.")
#
##Solving the encoding
#with open('set1challenge4.txt') as f:
#    lines = f.readlines()
#f.closed
#
#text = [x.strip() for x in lines]
#
#final = []
#for line in text:
#    binline = cushex.hexToBin(line)
#    for i in range(128):
#        letterbin = "{0:08b}".format(i)
#        letters = cusbitops.binToASCII(cusbitops.xor(binline,letterbin))
#        score = analyze.charfreq(letters)
#        transfer = [letterbin, letters, score]
#        final.append(transfer)
#final.sort(key=operator.itemgetter(2))
#for i in range(0,20):
#    print final[i]

##Set 1 Challenge 5
#key = "ICE"
#sen = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
#
#keybin = cusbitops.ASCIITobin(key)
#senbin = cusbitops.ASCIITobin(sen)
#print(cushex.binToHex(cusbitops.xor(senbin, keybin)))

##Set 1 Challenge 6
val1 = "this is a test"
val2 = "wokka wokka!!!"

print(analyze.hammingDistance(val1, val2))
