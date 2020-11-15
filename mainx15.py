# simple script for hashgames incl main

import sys
import os
import argparse
import random
import string
from hashlib import sha1

# pip install requests
import requests
import hashlib


def pwxused(pw):

    hash = hashlib.sha1(pw.encode("utf-8"))
    hashdig = hash.hexdigest()
    hashstr_l = hashdig[:5]
    hashstr_r = hashdig[5:]

    print(hashstr_l)
    print(hashstr_r)

    return False


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', title='command')
    subparsers.required = False
    parser_c = subparsers.add_parser('c', help='check x')
    parser_c.add_argument('password', help='password to check against database')
    args = parser.parse_args()

    if args.command == 'c':
        print("bravo t")
        password = args.password
        if pwxused(password):
            return 1
        return 0

    print("end")
    return 0


if __name__ == '__main__':
    sys.exit(main())
