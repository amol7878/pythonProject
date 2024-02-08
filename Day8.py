
info = ["chinmay","deshpande",22,33]
print(type(info))



# prgram
dictinfo =  {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":32,
    "rollNo":45
}
print(dictinfo)
print(type(dictinfo))


# program 2

#          0        1       2       3         4
listN = ["apple","mango","banana","grapes","banana"]
print(listN)
y1  = len(listN)
print(y1)
# list stores the value by index

vehicle = {
    #property:value
    #key:value
    "color":"red",
    "type":"sedane",
    "color":["yellow", "red"]
}
print(vehicle)
# It does not stores value by index

# program 3
animal = {
   "name":"tiger",
    "legs":4,
    "found":["india","bangladesh"]
}
q2 = len(animal)
print(q2)


# program 4

k = [11,22,33]
print(k[1])

MH = {
    "city1":"pune",
    "city2":"mumbai"
}
print(MH['city1'])
print(MH['city2'])

# add the property to dict
MH['city3'] = "wardha"
print(MH)

# update
MH['city2'] = "jaipur"
print(MH)

del MH['city3']
print(MH)


# program 5
bank = {
    "accNo":123,
    "bal":10000000000,
    "branch":"khardi",
    "city":"pune"
}

# retrive
print(bank["accNo"])

# add
bank["pincode"] = 411028
print(bank)

# udpate
bank['accNo'] = 456
print(bank)

# del
del bank['city']
print(bank)

# program 6
fruits = ["apple","mango","banana","papaya"]

for fr in fruits:
    print(fr)

for fruit in range(len(fruits)):
    print(fruits[fruit])






















