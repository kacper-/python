#!/usr/bin/python3

import sys


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)


if __name__ == '__main__':
    c = len(sys.argv)
    if c == 2:
        print(factorial(int(sys.argv[1])))
    else:
        if c == 1:
            print("no argument!")
        else:
            print("too many arguments!")
