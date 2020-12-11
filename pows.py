# primality testing

import sys
import os
import argparse
import random
import string

from models.BColors import BColors

def normal_exp():

    print("2^3 : " + str(2^3))
    print("2^3 % 5 : " + str(2^3 % 5))
    print("2**3 : " + str(2**3))
    print("2**3 % 5 : " + str(2**3 % 5))
    print("2**8 % 5 : " + str(2**8 % 5))
    print("(2**8)*6 % 5 : " + str((2**8)*6 % 5))
    print("2*6 % 5 : " + str(2*6 % 5))
    print("12*6 % 5 : " + str(12*6 % 5))
    print("12*7 % 5 : " + str(12*7 % 5))

    return 0


def pows(n): # 6k algo

    print("pow(2, 3) : " + str( pow(2, 3) ))
    print("pow(2, 3, 5) : " + str( pow(2, 3, 5) ))
    print("pow(2, 8, 5) : " + str( pow(2, 8, 5) ))

    print("(pow(2, 8))*6 % 5 : " + str((pow(2, 8))*6 % 5))
    print("(pow(2, 8, 5))*6 % 5 : " + str((pow(2, 8, 5))*6 % 5))
    print("pow(2*6, 1, 5) : " + str(pow(2*6, 1, 5)))
    print("12*6 % 5 : " + str(12*6 % 5))
    print("12 % 5 * 6 % 5 : " + str(12 % 5 * 6 % 5))
    print("12*7 % 5 : " + str(12*7 % 5))
    print("12 % 5 * 7 % 5 : " + str(12 % 5 * 7 % 5))

    try:
        assert(12*7 % 5 == 12 % 5 * 7 % 5)
        print("assert1 done")
        assert(12*7 % 5 == 12 % 5 * 7 % 6)
        print("assert2 done")
        pass
    except:
        print("Unexpected error:", sys.exc_info()[0])
        pass
        #raise

    return True


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', title='command')
    subparsers.required = False
    parser_c = subparsers.add_parser('c', help='check x')
    parser_c.add_argument('nr', help='check nr for primality')
    args = parser.parse_args()

    normal_exp()
    print(BColors.WARNING + "-----------------" + BColors.ENDC)
    pows(1234)

    print("end reached..")
    return 0

if __name__ == '__main__':
    sys.exit(main())
