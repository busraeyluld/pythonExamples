#students = ["john", "mark", "venessa", "mariam"]
#for student in students:
   # print(student.upper())
#-------------------------
salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary,end=",")

def new_salaries(salary, rate):
    return int(salary*rate/100 + salary)

for salary in salaries:
    updated_salary = new_salaries(salary, 20)
    print(updated_salary)
