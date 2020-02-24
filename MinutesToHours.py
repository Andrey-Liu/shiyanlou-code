#!/usr/bin/env python3
import sys

def Hours(minutes):
    if minutes < 0:
        raise ValueError("Input number cannnot be negative")
    else:
        count_h = minutes // 60
        count_m = minutes % 60
        print("{} H, {} M".format(count_h,count_m))


try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")

