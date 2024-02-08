#
# x = 10
# print(x)
# x = 100
# print(x)
#
# # Arithmetic
#
# q1 = 10
# q2 = 5
#
#
# print(q1+q2)
# print(q1-q2)
# print(q1*q2)
# print(q1/q2)
# print(q1%q2)
#
# q = 8
# r = 4
#
# print(q+r)
# print(q-r)
# print(q*r)
# print(q/r)
# print(q%r)
#
# #  10 pair 50 lines ---- DRY
#
# def Calculator(x,y):
#     print(x + y)
#     print(x - y)
#     print(x * y)
#     print(x / y)
#     print(x % y)
#
# Calculator(12,4)
# Calculator(4,2)
#
#
# # program 3
#
# # function without parameter and without return type
#
#
# def addA():
#     print(8+8)
#
# addA()
# addA()
# addA()
# addA()
# addA()

# # function with parameter and without return type
# def addB(x,y):
#     print(x+y)
#
# addB(12,4)
# addB(124,4)
# addB(1,2)
#
# # function with parameter and with return type
# # 100
# # 100
#
# def addC(x,y):
#      return x +y
#
# q1 = addC(12,3)
# print(q1)
# print(q1+q1)
# print(q1 * 0.10)
# print(q1 / 3)
#

# Types

# Introvert / Extrovert
# less social   more social
# less outing   more social
# calm          loud

# Human
# Properties - color , height ,weight ,gender
# Methods - talk() , walk()

# Vehicle
# Properties - color , type , model , name ,regNo
# Methods - start() , stop()

# Bank
# Properties - bal , accNo ,accType , accName , branch
# Methods - Deposit() , Withdraw()

x = 10
print(x)
print(type(x))
# 0 , 13,-13

y = 12.5
print(type(y))
# 23.5 , -34,0.45

z = True
print(z)
print(type(z))
# True False

q = 'chinmay'
print(q)
print(type(q))
# " ", "123" ,"QWE" ,"Wqwe#$#"

# comparison
# entity < entity -----> boolean --- type
# < , > ,<=, >= ,!= ,==

print(2 > 3)  # False
print(2 < 3)  # True
print(2 <= 3)  # True
print(3 >= 2)  # True
print(2 != 3)  # True
print(2 == 3)  # False
print(3 == 3)  # True

# logical operators

# and

# True  and  True  ====> True
# False  and  True  ====> False
# True   and  False ====> False
# False  and  False ====> False

print(3 == 3 and 7 != 6)
print(3 != 3 and 7 != 6)
print(3 == 3 and 7 == 6)
print(3 != 3 and 7 == 6)

# or

# True  or  True  ====> True
# False  or  True  ====> True
# True   or  False ====> True
# False  or  False ====> False

print(3 == 3 or 7 != 6)
print(3 != 3 or 7 != 6)
print(3 == 3 or 7 == 6)
print(3 != 3 or 7 == 6)

# not
print(not (7 == 7))
print(not (7 != 7))

h = """" chinmay\'s

 asfasfa

 asf"""

print(int(4.0))