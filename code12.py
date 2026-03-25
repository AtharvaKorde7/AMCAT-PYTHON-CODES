mydict = {
    "name": "prashant",
    "professional": "developer",
    "enpid": 1001
}
print(mydict)

mydict[102] = "peter"
print(mydict)

for x in mydict:
    print(x)

for x in mydict.values():
    print(x)

for x, y in mydict.items():
    print(x, y)

name = "prashantjha"
print(name[0:5])
print(name[::-1])