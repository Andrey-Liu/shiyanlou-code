#!/usr/bin/env python3
i = 1
print("-" * 50)
while i <= 10:
    for a in range(1,11):
        print("{:5d}".format(i * a), end=" ")
    i += 1
    print()
print("-" * 50)
