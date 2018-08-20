#!/usr/bin/python
import string

frequencyBase = { 'a': 8167, 'b': 1492, 'c': 2782, 'd': 4253, 'e': 12702, 'f': 2228, 'g': 2015, 
        'h': 6094, 'i': 6966, 'j': 153, 'k': 772, 'l': 4025, 'm': 2406, 'n': 6749, 'o': 7507, 
        'p': 1929, 'q': 95, 'r': 5987, 's': 6327, 't': 9056, 'u': 2758, 'v': 978, 'w': 2360, 
        'x': 150, 'y': 1974, 'z': 74}

def charfreq(value):
    value = value.replace(" ", "")
    value = value.lower()
    value = value.translate(None, string.punctuation)
    length = len(value)
    characters = list(set(value))
    score = 0

    for i in frequencyBase:
        #print abs(frequencyBase[i]  - int(100000*float(value.count(i))/length))
        score += abs(frequencyBase[i]  - int(100000*float(value.count(i))/length))
    return score
