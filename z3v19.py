# coding: utf-8
 
# z3-solver games

from z3 import *
 
def main():
	
    person = list()

    # TODO modify for writing database as csv
    fieldnames = ["Age", "Male", "Salary (k)"]

    s = Solver()
    age = IntVector('age', 10)
    male = BoolVector('male', 10)
    salary = IntVector('salary', 10)
    
    # Printing the mean 
    print("Mean is :", x)

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
