#!/usr/bin/env python3

# Fix Python 2.x.
from __future__ import print_function
try: input = raw_input
except NameError: pass

import random
#use good randomness generator
secure_rand = random.SystemRandom()

def print_flag():
    with open("./flag.txt", "r") as f:
        print(f.read())

def read_secure_primes():
    primes = []
    # list of 100 secure primes, all generated with secure methods
    # shared with the client so he can generate all private keys
    with open("./100_secure_primes.txt", "r") as f:
        for line in f:
            primes.append(int(line.strip()))
    return primes

def generate_RSA_pubkey(primes):
    p, q = secure_rand.sample(primes, 2)
    N = p * q
    e = 0x10001
    return (N,e)

def challenge():
    print("Welcome to the secret data store, please authenticate:")
    print("Authorized users should be in possession of the secret key list.")
    list_of_primes = read_secure_primes()
    N,e = generate_RSA_pubkey(list_of_primes)
    print("N = {}".format(N))
    print("e = {}".format(e))
    print("please sign the challenge c!")
    c = secure_rand.randint(0, N-1)
    print("c = {}".format(c))
    signature = input("signature of c:").strip()
    try:
        signature = int(signature)
        if pow(signature, e, N) == c:
            print("Hi, here is the data you stored:")
            print_flag()
        else:
            print("Incorrect signature, access denied!")
    except Exception as e:
        print("Invalid signature, access denied!")


if __name__ == "__main__":
    challenge()
