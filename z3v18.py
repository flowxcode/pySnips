# coding: utf-8
 
# z3-solver games

from z3 import *
 
def main(): 

    from z3 import *

    a = [1,2,3]

    s = Solver()
    x = Int('x')
    s.add(Or([x == i for i in a]))

    # Enumerate all possible solutions:
    while True:
        r = s.check()
        if r == sat:
            m = s.model()
            print m
            s.add(x != m[x])
        else:
            print r
            break

    ### approach2

    x = Int('x')
    y = Int('y')
    print(solve(x > 2, y < 10, x + 2*y == 7))
	
    person = list()

    # TODO modify for writing database as csv
    fieldnames = ["Age", "Male", "University Degree" , "Married", "Salary (k)"]

    s = Solver()
    age = IntVector('age', 10)
    male = BoolVector('male', 10)
    salary = IntVector('salary', 10)

    s.add([male[i] == False for i in range(10)])
    s.add(Sum([If(And(male[i] == False, salary[i] > 50), age[i], 0) for i in range(10)]) / (10 - 4) == 504)

    x = Int('x')

    s.add(age >= 18)
    s.add(age <= 100)
    # s.add(Or(male == True, male == False))
    s.add(male)
    s.add(degree)
    s.add(married)
    s.add(salary >= 20)
    s.add(salary <= 100)

    # s.add( Sum([If(And(male[i] == False, salary[i] > 50), age[i], 0) for i in range(10)]) / (10 - NUM_MALE) == 50 )

    # temp = (Sum([If(And(male[i] == False, salary[i] > 50), age[i], 0) for i in range(10)]) / (10 - NUM_MALE) == 50 )

    data1 = [1, 3, 4, 5, 7, 9, 2] 
  
    xt = statistics.mean(data1) 

    s.add(statistics.mean(x) == 5)
    
    # Printing the mean 
    print("Mean is :", x) 

    for i in range(10):
        if s.check() == sat:
            model = s.model()
            person.append([model[age], model[male], model[degree], model[married], model[salary]])
            s.add(Or(age != model[age], male != model[male], degree != model[degree], married != model[married], salary != model[salary]))

    with open(outfile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()

        for j in person:
            data = {fieldnames[0]: j[0]}
            data[fieldnames[1]] = j[1]
            data[fieldnames[2]] = j[2]
            data[fieldnames[3]] = j[3]
            data[fieldnames[4]] = j[4]

            writer.writerow(data)

            print(data)
        
        print(s.check())

    return 0


if __name__ == "__main__": 
	main() 
