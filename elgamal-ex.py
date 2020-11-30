#! /usr/bin/python

'''ElGamal with field mod prime p, not polynomial field.'''

from random import randint
from likelyPrime import isLikelyPrime

def findpg(bits, pFail):
  '''Return (p, q) where p has at least the specified number of bits,
  and is prime with probability at least 1-pFail, and g of order p-1.
  This can take some time.
  '''
  tries = 0
  while True:
    q = q0 = 1 + 2*randint(1<<(bits-2), 1<<(bits-1)) # odd
    while not isLikelyPrime(q, pFail):
      q = q + 2
    p = 2*q + 1
    if isLikelyPrime(p, pFail):
      break
    tries += (q-q0)/2
  print(tries, 'prime tries')
  # found p - now look for g of maximal order p-1 = 2q
  while True:
    g = randint(2, p-3)
    if g*g % p != 1 and pow(g,q,p) != 1: # order of g is 2, q, or p-1
       break
  return (p,g)

def keygen(p,g):
  ''' Generate public and private keys (A, a) given an odd prime p
  and a primitive root g.
  '''
  a = randint(2,p-2)
  A = pow(g,a,p)
  return (A,a)

def encrypt(p,g,A,n):
  '''Encrypt number n given the public key p,g,A'''
  # first find (B,b)
  (B,b) = keygen(p,g)
##  print 'b', b
  return (B,n*pow(A, b, p)%p)

def decrypt(p,g,a,cipherpair):
  '''Decrypt a cipher pair (B,c) given the private key p,g,a.'''
  (B,c) = cipherpair
  return c*pow(B,p-1-a,p) % p
  

def tester():
  bits = 200
##  bits = 5
  (p,g)=findpg(bits, 10**-6)
  (A,a)=keygen(p,g)
  msg = 123456789123456789123456789123456789123456789123456789
  assert msg < p
  print(bits, 'bit prime ', p)
  print('g', g)
  print('A', A)
  print('a', a)
  print('msg:', msg)
  cipherpair = encrypt(p,g,A, msg)
  (B, cipher) = cipherpair
  print('B', B)
  print('cipher', cipher)
  decrypted = decrypt(p,g,a, cipherpair)
  print('decrypted:', decrypted)
  print('match?', decrypted == msg)

if __name__ == '__main__':
  tester()
