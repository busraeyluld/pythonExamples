#divide_students func yazınız
#çift indexte yer alan öğrencileri bir listeye tektekileri başka bir listeye ekle
#fakat bu iki liste tek bir liste olarak return olsun(dönsün).
students = ["john", "mark", "venessa", "mariam"]
def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups
divide_students(students)

#2.yol:
for index, student in enumerate(students):
    print(index, student)
A = []
B = []
for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)
print(A)
print(B)
