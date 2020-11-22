# original gist from shahril96/garden_puzzle_z3.py
# z3 games

import sys
import itertools
from z3 import *

# Create to bit-vectors of size 32
x, y = BitVecs('x y', 32)

print("solve 1:")
solve(x + y == 2, x < 0, y > 0)

# Bit-wise operators
# & bit-wise and
# | bit-wise or
# ~ bit-wise not
print("solve 2:")
solve(x & y == ~y)

print("solve 3:")
solve(x < 0)

# using unsigned version of < 
print("solve 4:")
solve(z3.ULT(x, 0))
print("---------------")

x, y = BitVecs('x y', 32)

solve(x >> 2 == 3)
solve(x << 2 == 3)
solve(x << 2 == 24)

# =========================================================== #

person = {"luke": 0, "sam": 1, "paul": 2, "hank": 3, "zick": 4}

'''
# Crops
[0] (0x40) Fruits     -> Apple, Pear, Nut, Cherry
[1] (0x20) Vegetables -> Carrot, Parsley, Gourd, Onion
[2] (0x10) Flowers    -> Aster, Rose, Tulip, Lily 

Structure of crops :-
< 3 bits : type of crop > < 4 bits : each of crops >

eqs:
100 1000 = fruit crop, apple type
010 0001 = vegetable crop, onion type
001 0010 = flower crop, tulip type
'''

crops = {
    "apple"  : 0x48,  "pear"   : 0x44, "nut"   : 0x42, "cherry": 0x41,
    "carrot" : 0x28,  "parsley": 0x24, "gourd" : 0x22, "onion" : 0x21,
    "aster"  : 0x18,  "rose"   : 0x14, "tulip" : 0x12, "lily"  : 0x11
}

# =========================================================== #

# list structure: <garden owner> <crop> <crop> <crop> <crop>
table = [ BitVecs('go_%d0 c_%d1 c_%d2 c_%d3 c_%d4' % tuple([i]*5), 32) for i in range(5) ]

print(table)
print(type(table[0][0]))

s = Solver()

for v in crops.items():
    print(v[0])

# constrain the table values (fact 3 & 1)
for i in range(5):
    s.add(table[i][0] >= 0, table[i][0] <= 4)  # person 0-based index
    s.add(And([Or([table[i][j] == v[1] for v in crops.items()]) for j in range(1, 5)]))

# make sure people are distinct
s.add(Distinct([table[i][0]  for i in range(5)]))

# 2. Everybody grows exactly 4 different varieties.
s.add([Distinct([table[i][j]  for j in range(5)])  for i in range(5)])

for comb in itertools.combinations(range(5), 4):
    print(comb)

# 4. Only one variety is in 4 gardens. 
constrain = []
for v in crops.items(): # 12
    for comb in itertools.combinations(range(5), 4): # results in 5 combination lines with 4 items
        p = And([Or([table[i][j] == v[1]  for j in range(1,5)])  for i in comb])
        q = And([And([table[i][j] != v[1]  for j in range(1,5)])  for i in range(5) if i not in comb])
        constrain.append(And(p, q))
s.add(Or(constrain))

print(constrain)
# logic for one of the 12 crops. parent-OR contains 5 * 12crops = 60 And-blocks
# on crop must be in 4 gardens (And) , but must not in the 5th
# there are 5 combinations C(n,r) = C(5,4) = 5
# one of these 5 must be True.
# overall 5 * 12crops = 60 blocks containend in the parent-OR
'''
And(
    And(
        Or(c_01 == 72, c_02 == 72, c_03 == 72, c_04 == 72),
        Or(c_11 == 72, c_12 == 72, c_13 == 72, c_14 == 72),
        Or(c_21 == 72, c_22 == 72, c_23 == 72, c_24 == 72),
        Or(c_31 == 72, c_32 == 72, c_33 == 72, c_34 == 72)
    ),
    And(
        And(c_41 != 72, c_42 != 72, c_43 != 72, c_44 != 72)
    )
), 

And(And(Or(c_01 == 72, c_02 == 72, c_03 == 72, c_04 == 72),
    Or(c_11 == 72, c_12 == 72, c_13 == 72, c_14 == 72),
    Or(c_21 == 72, c_22 == 72, c_23 == 72, c_24 == 72),
    Or(c_41 == 72, c_42 == 72, c_43 == 72, c_44 == 72)),
And(And(c_31 != 72, c_32 != 72, c_33 != 72, c_34 != 72))), 

And(And(Or(c_01 == 72, c_02 == 72, c_03 == 72, c_04 == 72),
    Or(c_11 == 72, c_12 == 72, c_13 == 72, c_14 == 72),
    Or(c_31 == 72, c_32 == 72, c_33 == 72, c_34 == 72),
    Or(c_41 == 72, c_42 == 72, c_43 == 72, c_44 == 72)),
And(And(c_21 != 72, c_22 != 72, c_23 != 72, c_24 != 72))), 

And(And(Or(c_01 == 72, c_02 == 72, c_03 == 72, c_04 == 72),
    Or(c_21 == 72, c_22 == 72, c_23 == 72, c_24 == 72),
    Or(c_31 == 72, c_32 == 72, c_33 == 72, c_34 == 72),
    Or(c_41 == 72, c_42 == 72, c_43 == 72, c_44 == 72)),
And(And(c_11 != 72, c_12 != 72, c_13 != 72, c_14 != 72))), 

And(And(Or(c_11 == 72, c_12 == 72, c_13 == 72, c_14 == 72),
    Or(c_21 == 72, c_22 == 72, c_23 == 72, c_24 == 72),
    Or(c_31 == 72, c_32 == 72, c_33 == 72, c_34 == 72),
    Or(c_41 == 72, c_42 == 72, c_43 == 72, c_44 == 72)),
And(And(c_01 != 72, c_02 != 72, c_03 != 72, c_04 != 72))), 
'''

# 5. Only in one garden are all 3 kinds of crops. 
# 0x70 of logical pipe Ors 111000 means all three first bits are set, means all varietes exist
constrain = []
for i in range(5):
    p = []
    for j in range(5):
        eq = And( (table[j][1] | table[j][2] | table[j][3] | table[j][4]) & 0xf0 == 0x70 )
        p.append(eq)
        if j != i:
            p[-1] = Not(p[-1]) # make the last entry a Not

    constrain.append(And(p))
s.add(Or(constrain))
# print(constrain)


# 6. Only in one garden are all 4 varieties of one kind of crops.
constrain = []
for i in range(5):
    p = []
    for j in range(5):
        eq = And(table[j][1] & 0xf0 == table[j][2] & 0xf0,
                 table[j][2] & 0xf0 == table[j][3] & 0xf0,
                 table[j][3] & 0xf0 == table[j][4] & 0xf0)
        p.append(eq)
        if j != i:
            p[-1] = Not(p[-1])
    constrain.append(And(p))
s.add(Or(constrain))
print(constrain)


# 7. Pear is only in the two border gardens.
print([Or([table[j][i] == crops['pear']  for i in range(1, 5)]) for j in [0, 4]])
s.add(And([Or([table[j][i] == crops['pear']  for i in range(1, 5)]) for j in [0, 4]]))
s.add([table[j][i] != crops['pear']  for j in range(1, 4)  for i in range(1, 5)])



# 8. Paul's garden is in the middle with no lily.
s.add(table[2][0] == person['paul'])
s.add([table[2][i] != crops['lily']  for i in range(1, 5)]) # can't be lily

print([table[k][j] != crops['aster']  for k in range(5) if k != 0  for j in range(1, 5)])

# 9. Aster grower doesn't grow vegetables.
for i in range(5):
    p = Or([table[i][j] == crops['aster']  for j in range(1, 5)])
    q = [table[k][j] != crops['aster']  for k in range(5) if k != i  for j in range(1, 5)] # filter other than `i` can't be an aster
    q = q + [table[i][j] & 0x20 == 0x0  for j in range(1, 5)] # no vegetable
    s.add(Implies(p, And(q)))
# q first
'''
00:c_11 != 24
01:c_12 != 24
02:c_13 != 24
03:c_14 != 24
04:c_21 != 24
05:c_22 != 24
06:c_23 != 24
07:c_24 != 24
08:c_31 != 24
09:c_32 != 24
10:c_33 != 24
11:c_34 != 24
12:c_41 != 24
13:c_42 != 24
14:c_43 != 24
15:c_44 != 24
16:c_01 & 32 == 0
17:c_02 & 32 == 0
18:c_03 & 32 == 0
19:c_04 & 32 == 0
'''

# 10. Rose growers don't grow parsley.
for i in range(5):
    p = Or([table[i][j] == crops['rose']  for j in range(1, 5)])
    q = And([table[i][j] != crops['parsley'] for j in range(1, 5)])
    s.add(Implies(p, q))



# 11. Nuts grower has also gourd and parsley.
for i in range(5):
    p = Or([table[i][j] == crops['nut']  for j in range(1, 5)])
    exc = And([table[k][j] != crops['nut']  for k in range(5) if k != i  for j in range(1, 5)]) # another garden can't have nuts
    q = Or([table[i][j] == crops['gourd']  for j in range(1, 5)])
    r = Or([table[i][j] == crops['parsley']  for j in range(1, 5)])
    s.add(Implies(p, And(q, r, exc)))



# 12. In the first garden are apples and cherries.
p = Or([table[0][j] == crops['apple']  for j in range(1, 5)])
q = Or([table[0][j] == crops['cherry']  for j in range(1, 5)])
s.add(And(p, q))



# 13. Only in two gardens are cherries.
constrain = []
for comb in itertools.combinations(range(5), 2):
    p = And([Or([table[i][j] == crops['cherry']  for j in range(1,5)])  for i in comb])
    q = And([And([table[i][j] != crops['cherry']  for j in range(1,5)])  for i in range(5) if i not in comb])
    constrain.append(And(p, q))
s.add(Or(constrain))



# 14. Sam has onions and cherries.
for i in range(5):
    p = Or([table[i][j] == crops['onion']  for j in range(1, 5)])
    q = Or([table[i][j] == crops['cherry']  for j in range(1, 5)])
    s.add(Implies(table[i][0] == person['sam'], And(p, q)))



# 15. Luke grows exactly two kinds of fruit.
# implementation: only first 1 and 2 crops are fruit
for i in range(5):
    p = And([table[i][j] & 0x40 == 0x40 for j in range(1,3)])
    q = And([table[i][j] & 0x40 == 0x00 for j in range(3,5)])
    s.add(Implies(table[i][0] == person['luke'], And(p, q)))



# 16. Tulip is only in two gardens.
constrain = []
for comb in itertools.combinations(range(5), 2):
    p = And([Or([table[i][j] == crops['tulip']  for j in range(1,5)])  for i in comb])
    q = And([And([table[i][j] != crops['tulip']  for j in range(1,5)])  for i in range(5) if i not in comb])
    constrain.append(And(p, q))
s.add(Or(constrain))



# 17. Apple is in a single garden.
for i in range(5):
    p = Or([table[i][j] == crops['apple']  for j in range(1, 5)])
    q = [table[k][j] != crops['apple']  for k in range(5) if k != i  for j in range(1, 5)]  # other gardens can't have apple
    s.add(Implies(p, And(q)))



# 18. Only in one garden next to Zick's is parsley.
s.add(table[4][0] != person['zick']) # zick can't be the last person
for i in range(4):
    p = [Or([table[i+1][j] == crops['parsley']  for j in range(1, 5)])]
    p = p + [table[k][j] != crops['parsley']  for k in range(5) if k != i+1  for j in range(1, 5)]
    s.add(Implies(table[i][0] == person['zick'], And(p)))



# 19. Sam's garden is not on the border.
s.add([table[i][0] != person['sam'] for i in [0,4]])



# 20. Hank grows neither vegetables nor asters.
for i in range(5):
    p = [And(table[i][j] & 0x20 == 0x0, table[i][j] != crops['aster']) for j in range(1, 5)]
    s.add(Implies(table[i][0] == person['hank'], And(p)))



# 21. Paul has exactly three kinds of vegetable.
# implementation: index 1-3 contains only vegetable
s.add([table[2][i] & 0x20 == 0x20 for i in range(1, 4)])
s.add(table[2][4] & 0x20 == 0x00)  # one more crop can't be vegetable


# =========================================================== #


def print_ans(m):
    
    table_str = [[None for _ in range(5)] for _ in range(5)]
    res_ppl = dict((v,k) for k,v in person.items())
    res_crops = dict((v,k) for k,v in crops.items())
    
    for key in m:

        val = int(m[key].__str__())
        key = key.__str__()

        if "go_" in key: table_str[int(key[3])][0] = res_ppl[val]
        else:            table_str[int(key[2])][int(key[3])] = res_crops[val]

    print("")
    for i in range(5):
        sys.stdout.write(" | ")
        for j in range(5):
            sys.stdout.write("%7s | " % (table_str[i][j].upper() if j==0 else table_str[i][j]))
        print("")

if s.check() == sat:
    print_ans(s.model())
    
    stats = s.statistics()
    print(stats)

    # should print below answer (without same ordering)
    '''
    |    HANK |  cherry |    pear |    rose |   apple | 
    |     SAM |   tulip |  cherry |    rose |   onion | 
    |    PAUL |   onion |  carrot |   gourd |    rose | 
    |    ZICK |   aster |    lily |   tulip |    rose | 
    |    LUKE |     nut |    pear | parsley |   gourd |
    '''
