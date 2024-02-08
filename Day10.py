info = {
        "firstName":"chinmay",
        "lastName":"deshpande",
        "rollNo":34,
        "city":"pune"

}
print(info)
print(type(info))
info2 = info
info2['firstName'] = "ram"
print(info)
print(info2)

a = 123
vehicle = {
        "color":"red",
        "type":"sedane",
        "regno":a
}

print(vehicle)

vehicle2  = vehicle.copy()
vehicle2['color'] = "blue"
print(vehicle2)
print(vehicle)

vehicle2["regno"] = 345
print(vehicle2)


# program 3

vehicle = {
        "color":"red",
        "type":"sedane",
        "regno":a
}

# program 4
# pop() - removes
vehicle.pop('color')
print(vehicle)

# program 5

b = vehicle2.get('Type')
print(b)
#print(vehicle2['Type'])


# program 6


info3 = {
        "firstName":"chinmay",
        "lastName":"deshpande",
        "age":23,
        "rollNo":45
}

for x in info3:
        print(x,info3[x])

for prop in info3.keys():
        print(prop)

for val in info3.values():
        print(val)

for item in info3.items():
        print(item)

# info3.clear()
# print(info3)
# fromkeys()
x = ("name","age","rollNo")
y = None
q1 = dict.fromkeys(x,y)
print(q1)

# update()
q1.update({"name":"chinmay"})
q1.update({"lang":"hindi"})
print(q1)


info3 = {
        "language":"hindi",
        "city":"pune",
        "country":"India"
}

info3.popitem()
print(info3)
q1 = info3.setdefault("language",None)
print(q1)