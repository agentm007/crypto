#!/usr/bin/python

charSet = []
upperCase = range(65,91)
lowerCase = range(97,123)
nums = range(48,58)
charSet.extend(upperCase)
charSet.extend(lowerCase)
charSet.extend(nums)
charSet.append(42)
charSet.append(47)

for i in range(64):
    print "\"" + chr(charSet[i])  + "\": " + "\"{:06b}".format(i) + "\","

for i in range(64):
    print "\"{:06b}".format(i) + "\": " + "\"" + chr(charSet[i]) + "\","
