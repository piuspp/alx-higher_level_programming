#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= 97 and i <= 123:
            i = chr(ord(i)-32)
        print("{}".format(i), end=' ')
    Print("")
