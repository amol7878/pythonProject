
# program  1
def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

# q1 = isEven(10)
# print(q1)

listA = [11,22,33,44,55,66,7,33,44,55,66,73]
x1 = list(filter(isEven,listA))
print(x1)

x2 = list(filter(lambda x : x % 2 == 0,listA))
print(x2)

# program 2  above50
marks = [22,33,44,55,22,33,44,55,66,77]
x3 = list(filter(lambda x: x > 50,marks))
print(x3)


# program 3 map()

def sqr(x):
    return x * x
print(sqr(2))

listN = [1,2,3,4,5]
x4 = list(map(sqr,listN))
print(x4)
x5 = list(map(lambda x:x*x,listN))
print(x5)

# program 4
a = [11,22,33]
b = [44,55,66]
x6 = list(map(lambda x,y:x*y,a,b))
print(x6)

#program 5
birthYear = [1989,1990,1991,1992]
x7 = list(map(lambda  x : 2023 -x ,birthYear))
print(x7)

#program 6
from functools import  *
listA = [11,22,33]
total = 0
for i in listA:
    total = total + i
print(total)

x8 = reduce(lambda x,y:x+y,listA)
print(x8)

# program 7

from functools import reduce

people = [
    {
        'name': 'Alice',
        'age': 30 ,
        'city':"pune",
        "skills":["python","java","javascript"]
    },
    {
        'name': 'Bob',
        'age': 22,
        'city':"sangamner",
        "skills":["css3","sql","powerBI"]

    },
    {
        'name': 'Charlie',
        'age': 28,
        'city':"pune",
        "skills":["css3","sql","powerBI"]
    },
    {
        'name': 'David',
        'age': 26,
        'city':"nagpur",
        "skills":["css3","flutter","c#"]
    },
    {
        'name': 'Eve',
        'age': 19,
        'city':"jaipur",
        "skills":["css3","flutter","c#"]
    }
]

# program 1

# all cities
#people = [dic1,dic2,dic3,dic4,dict5]

listA = [11,22,33,44,55,66]
# [12,23,34,45,56,67]
print(list(map(lambda x:x+1,listA)))

# program 1
print(list(map(lambda person:person.get('city'),people)))

#program 2
# add  git as skill to every people
print(list(map(lambda person:person['skills'].append("git"),people)))
print(people)
for x in people:
    x['skills'].append("salesforce")
print(people)

# people belong to pune city
# program3
q1 = list(filter(lambda person: person['city'] == "pune",people))
for a in q1:
    print(a['name'])

# program 4
# alice:3
q2 = list(map(lambda person:person['name']+":" + str(len(person['skills'])),people))
print(q2)

# program 5
j = [11,22,33]
print(reduce(lambda acc,y:acc+y,j,5))
print(reduce(lambda acc,person:acc+person['age'],people,0)/len(people))






















































