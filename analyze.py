#!/usr/bin/python
import string

def analyze(value):
    value = value.replace(" ", "")
    value = value.lower()
    value.translate(None, string.punctuation)
    characters = list(set(value))

