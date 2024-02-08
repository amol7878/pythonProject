
# program 1

print("Hello")
x = 100
print(x)
x = 300
print(x)


# program 2
# Arithmetic operation
# Addition       +
# Subtraction    -
# Multiplication *
# Division       /
# Modulus        %


s = 10
t = 5

print(s+t)
print(s-t)
print(s*t)
print(s/t)
print(s%t)


print(23% 5)

q = 8
r = 4

print(q+r)
print(q-r)
print(q*r)
print(q/r)
print(q%r)

# DRY ----- Don't repeat yourself
# 10 pair --- 50 lines
def Calculator(x,y):
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y)

Calculator(12,4)
Calculator(8,4)
Calculator(9,3)


# function without parameter and without return type
def addA():
    print(5+5)
addA()
addA()
addA()
addA()
addA()
addA()

# function with parameter and without return type
def addB(x,y):
    print(x+y)
addB(12,4)
addB(12,3)
addB(10,4)

# function with parameter and with return type
def addC(x,y):
    return x + y
q1 = addC(2,3)
print(q1)
print(q1 + q1)
print(q1 * 0.10)
print(q1 - 2)

def subA(x,y):
     return x -y
q2 = subA(10,5)
#q2 = 5

def mul(x,y):
    return x * y
q3 = mul(q2,5)
print(q3)