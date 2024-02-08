
# program 1
numbers = [1,2,3,4,5,6,7,8,9,10]
newList = []
for item in numbers:
    newList.append(item * item)
print(newList)

# [expression for item in iterable if condition]
q2 = [item * item for item in numbers]
print(q2)

#program 2
names = ["amol","ram","rakesh","kajal","sarika","mayuri","chinmay","amol"]
q3 = [name.upper() for name in names]
print(q3)

#program3
q4 = [item.upper() for item in names if len(item) >= 5]
print(q4)

#program 4
q5 = [item * item * item for item in range(1,11)]
print(q5)

#program 5
students = [
    {'fullName':"chinmay deshpande",'age': 22},
    {'fullName':"sarang deshpande",'age': 30},
    {'fullName':"kanchan deshpande",'age': 50},
]

q5 = [student for student in students if student['age'] >= 30]
print(q5)



q5 = [student for student in students if student['age'] >= 30 and student['fullName'].startswith("k")]
print(q5)

#program 6

birthYear = [2001,1999,1998,1999,2000]
q6 = [2023 - year for year in birthYear ]
print(q6)

q7 = list(map(lambda year:2023 - year,birthYear))
print(q7)


q8 = list(filter(lambda student:student['age'] >= 30,students))
print(q8)

# list comprehension
#[1,2,3]
# reduce



