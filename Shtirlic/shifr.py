import random
__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-


class Monoalphabet:
    alphabet = 'ъшглсхаизчнцойвьпрыжюдяэтбекмуфщё'

    def __init__(self, keytable):
        lowercase_code = {self.alphabet[i]:keytable[i] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():keytable[i].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = {}  # FIXME

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        pass  # FIXME

key = []
f = open('keytable.txt','r')
for t in f.readlines():
    key.append(t[4])
print(key)
f2 = open('text3.txt','r')
cipher = Monoalphabet(key)
line  = f2.readline()
while line:
    print(cipher.encode(line))
    line = f2.readline()