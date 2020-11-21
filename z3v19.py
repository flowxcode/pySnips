# coding: utf-8
 
# z3-solver games

import statistics
from z3 import *




def main():

    arr = [tuple([i]*5) for i in range(5)]



    table = [ BitVecs('go_%d0 c_%d1 c_%d2 c_%d3 c_%d4' % tuple([i]*5), 32) for i in range(5) ]
    print(table)
    
    print(table[0])
    print(table[0][0])


    for r in table:
        for c in r:
            print(c,end = " ")
        print()
  
    # unsorted list of random integers 
    data1 = [2, -2, 3, 6, 9, 4, 5, -1] 
    print("Median of data-set is : % s " % (statistics.median(data1)))

    data1 = [234, -2, 3, 62, 9, 4, 5, -1, 1, 1, 1, 1, 1, 1, 1, 1]
    print("Median of data-set is : % s " % (statistics.median(data1)))
	
    person = list()


    # TODO modify for writing database as csv
    fieldnames = ["Age", "Male", "Salary (k)"]

    s = Solver()
    age = IntVector('age', 10)
    male = BoolVector('male', 10)
    salary = IntVector('salary', 10)    

    s.add([18 <= age[i] for i in range(10)])
    s.add([100 >= age[i] for i in range(10)])
    s.add([20 <= salary[i] for i in range(10)])
    s.add([100 >= salary[i] for i in range(10)])

    print(Sum([age[i] for i in range(10)]) / (4) == 58)
    print(Sum([If(And(male[i] == True, True), age[i], 0) for i in range(10)]) / (4) == 59)

    print([age[i] for i in range(10)])
    # print(medianx([age[i] for i in range(10)]))
    # if statistics.median([age[i] for i in range(10)]) == 1:
    #     print(1)

    print(sorted([0,3,2]))


    s.add(Sum([If(And(male[i] == True, True), age[i], 0) for i in range(10)]) / (4) == 59)
    s.add(Sum(sorted( [age[i] for i in range(10)] ))==1)

    s.add(Sum(sorted([age[i] for i in range(10)]))/2 == 1)
    s.add(medianx([age[i] for i in range(10)]) == 69)

    for i in range(10):
        if s.check() == sat:
            model = s.model()
            person.append([model[age[i]], model[male[i]], model[salary[i]]])
            s.add(Or(age[i] != model[age[i]], male[i] != model[male[i]], salary[i] != model[salary[i]]))

    for j in person:
        data = {fieldnames[0]: j[0]}
        data[fieldnames[1]] = j[1]
        data[fieldnames[2]] = j[2]

        print(data)
    
    print(s.check())

    return 0


if __name__ == "__main__": 
	main() 
