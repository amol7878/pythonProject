

# string booelan int float list

listA = ["poorva","abhisha","sarika","ram"]
# add
listA.append("jerry")
print(listA)
# retrive
print(listA[1])
# remove
listA.pop(1)
# update
listA[0] = "amol"
print(listA)

# program 2
dictB = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23
 }
print(type(dictB))

# retrive
print(dictB['firstName'])

# update
dictB['firstName'] = "tanmay"
print(dictB)

# add
dictB['city'] ="pune"
print(dictB)

# delete
del dictB['lastName']
print(dictB)


# loop
country  = ["india","pakistan","china","australia","cuba"]

# normal

for city in country:
    print(city)

for city in range(len(country)):
    print(country[city])


# dict

info3 = {
    "fullName":"chinmay deshpande",
    "skills":["python","java"],
    "age":32,
    "city":"pune",
    "canDrive":True,
    "city":"nagpur"
}

print(info3)
print(info3)

for prop in  info3:
    print(prop,info3[prop])


l = [11,22,33]
k = l
k[0] = 111
print(k) # [111,22,33]
print(l) # [111,22,33]

vehicle = {
        "color":"red",
        "city":"nagpur",
        "regNo":123
}
vehicle2  = vehicle
vehicle2['color'] = "blue"
print(vehicle)
print(vehicle2)




















