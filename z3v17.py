# coding: utf-8
 
# z3-solver games
# Z3 is a theorem prover from Microsoft Research with support for bitvectors, 
# booleans, arrays, floating point numbers, strings, and other data types.

from z3 import *
 
def main(): 
	
    s = Solver()
    x = Int('x')
    y = Int('y')
    s.add(x < 10)
    s.add(x > 0)
    s.add(y < 10)
    s.add(y > 0)
    s.add(x + y == 3)
    i = 0
    while s.check() == sat:
        print("Model %s:" % i)
        model = s.model()
        print("%s = %s" % (x, model[x]))
        print("%s = %s" % (y, model[y]))
        s.add(Or(x != model[x], y != model[y]))
        i = i + 1


if __name__ == "__main__": 
	main() 
