#!/usr/bin/env python3
# diference betwen a and global a:
def change():
    a = 90
    print(a)
a = 9
print("Before the function call ", a)
print("inside change function", end=' ')
change()
print("After the function call ", a)

