#!/usr/bin/env python3
import sys
if len(sys.argv) < 2:
    print("Wrong parameter!")
    print("./FindDigits.py file")
print("Target file: ", sys.argv[1])
fd = open(sys.argv[1])
a =''
for char in fd.read():
    if char.isdigit():
        a += char
print(a)
