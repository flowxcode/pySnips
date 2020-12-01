#! /usr/bin/python

'''Implementation of the Miller-Rabin primality test.  '''

from random import randint
# import gcd
from math import log
# from math import pow
from math import gcd

from mrabingfg import *

def isMillerRabinPsuedoPrime(n,a):
  if n % 2 == 0:
    return False #even numbers aren't prime
  m = n-1; k = 0
  #find number of times 2 divides n-1
  while m % 2 == 0:
    m = int(m/2)
    k = k + 1
#   y = pow(a,m,n)
  y = pow(a,m,n)
  if y == 1:
    return True
  for i in range(k):
    if y == n-1:
      return 1
    y = y*y % n
  return False

  

def isLikelyPrime(n, pFail):
  '''Return True if n is prime with probability > 1 - pFail.
  Return False if n is found to be composite.
  >>> isLikelyPrime(12304079, 10**-10)
  True
  >>> isLikelyPrime(32451611, 10**-10)
  True
  >>> isLikelyPrime(12304079*32451611, 10**-10)
  False
  '''
  t = int(1 - log(pFail)/log(4)) # use conservative fraction witnessses > 3/4
  for i in range(t):
    a = randint(1,n-1)
    #if gcd(a,n) != 1 or not isMillerRabinPsuedoPrime(n,a):
    if gcd(a,n) != 1 or not miillerTest(n,a):
      return False    
  return True

def likelyPrime(bits, pFail):
    '''Return a random number with the specified number of bits that is prime
    with probability > 1 - pFail.'''

    assert bits > 1, 'No 1-bit prime'
    nLow = (1 << (bits-1)) + 1
    nHigh = (1 << bits) - 1
    while(True):
        n = randint(nLow, nHigh)
        if isLikelyPrime(n, pFail):
            return n
    
##  Practical testing shows the 1/4 inaccuracy bound in Miller-Rabin
##  is extremely conservative.
def fractionFailMillerRabin(n, tries):
  '''n is the number to test for the given number of tries.
  Return the fraction of Miller-Rabin tests not passed.
  '''
  count = 0
  for i in range(tries):
    a = randint(1,n-1)
    if gcd(a,n) != 1 or not isMillerRabinPsuedoPrime(n,a):
       count += 1
  return 1.0*count/tries

if __name__ == '__main__': 
    import doctest
    doctest.testmod() #verbose=True) 

    
    