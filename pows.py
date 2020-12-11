# primality testing

import sys
import os
import argparse
import random
import string

from models.BColors import BColors

# framework

def normal_exp():

    return 0


def pows(n): # 6k algo

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

