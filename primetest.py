# primality testing

import sys
import os
import argparse
import random
import string

from models.BColors import BColors


# framework

def mock(): # part of 6kpm1 optimization
    n = 757
    i = 5
    while i ** 2 <= n:
        print("i:" + str(i) + ", n:" + str(n))
        if n % i == 0 or n % (i + 2) == 0:
            print("break")
            break
        i += 6    
    print("the end")


def isprime(x): # dumb stub as framework
    for i in range(2, x-1):
        if x % i == 0:
            print(BColors.WARNING + "oooohh noooooooooo" + BColors.ENDC)
            return False
        else:
            print(BColors.OKCYAN + "Christmas got a present for you. Its a prime number" + BColors.ENDC)
            return True


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', title='command')
    subparsers.required = False
    parser_c = subparsers.add_parser('c', help='check x')
    parser_c.add_argument('nr', help='check nr for primality')
    args = parser.parse_args()

    if args.command == 'c':
        print("args recieved..")
        nr = args.nr
        if isprime(int(nr)):
            return 0
        return 1

    if args.command is None:
        print("noooo arg......... testing 11")
        if isprime(56243542345434):
            return 0
        return 1

    print("end reached..")
    return 0

if __name__ == '__main__':
    sys.exit(main())

