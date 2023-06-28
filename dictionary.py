di = dict(r='red', b='blue', g='green')
print(di, type(di))

d = {"r": "red", "g": "green", "b": "blue"}
print(d, type(d))

d1 = dict()
d2 = {}

d = {"r": "red", "g": "green", "b": "blue"}

print(d["r"], d["b"])

d = {}
print(d, id(d))
d['c'] = "cyan"
d['b'] = "black"
print(d, id(d))

d['b'] = "brown"
print(d, id(d))

del (d['c'])
print(d, id(d))

d1 = {"r": "red", "g": "green", "b": "blue"}
d2 = {"b": "blue", "r": "red", "g": "green"}
print(d1 == d2)

d = {
    1: "int",
    12.4: "float",
    True: "bool",
    12 + 6j: "complex",
    (12,): "tuple",
    "james": "str"
}

print(d)

print(d1.keys())
print(d1.values())
print(d1.items())

for k in sorted(d1, reverse=True):
    print(k, d1[k])

stu = {
    "James": [70, 80, 60],
    "Blake": [56, 45, 21],
    "Neena": [45, 77, 66]
}

stu = {
    "James": {"C": 70, "CPP": 80, "Python": 60},
    "Blake": {"C": 56, "CPP": 45, "Python": 21},
    "Neena": {"C": 45, "CPP": 77, "Python": 66}
}

for name, details in stu.items():
    print(name, end=" ")
    for sub, marks in details.items():
        if (marks >= 50):
            print(sub, ":", "Pass", end=" ")
        else:
            print(sub, ":", "Fail", end=" ")
    print()

print(stu["Neena"]["Python"])

d = {}
count = int(input("no of keys"))
for i in range(count):
    key = eval(input("Enter Key"))
    value = eval(input("Enter Value"))
    d[key] = value

print(d)

d = {}
count = int(input("no. of keys"))
for i in range(count):
    key = eval(input("Enter Key"))
    value = eval(input("Enter value"))
    d[key] = value

print(d)

d = {}
d.setdefault("James", [12, 23, 34])
d["King"] = [34, 45, 456]
d.setdefault("James", [11, 11, 11])
d.clear()

d = {"r": "red", "g": "green", "b": "blue"}
d2 = dict.fromkeys(d, "Na")

for i in dir(dict):
    if not i.startswith("_"):
        print(i, end="   ")

print()

d = {}
d1 = {"r": "red"}
d2 = {"g": "green"}
d3 = {"b": "blue"}

for i in d1, d2, d3:
    d.update(i)

print(d)

# print(d.pop("r"))
print(d.popitem())
print(d)

d = {1: "one", 2: "two", 3: "three", 4: "four"}
print(d[6])
print(d.get(6))

"""
Write a Python script to add a key to a dictionary
"""
d = {0: 100, 1: 202}
d.update({2: 306})
print(d)

"""

Write a Python program to concatenate following dictionaries 
to create a new one.
"""

d1 = {1: 100, 2: 200}
d2 = {3: 300, 4: 400}
d3 = {5: 500, 6: 600}
d4 = {}
for d in (d1, d2, d3): d4.update(d)
print(d4)

"""
 Write a Python program to check if a given key already exists 
in a dictionary.

"""
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
n = int(input("Key to find in given list: "))


def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')


print(is_key_present(n))

"""
Write a Python script to print a dictionary where the keys are 
numbers between 1 and 15 (both included) and the values are square of keys
"""
d = dict()
for x in range(1, 16):
    d[x] = x ** 2
print(d)

"""
Write a Python program to sum all the items in a dictionary
"""

dict = {'a': 100, 'b': 200, 'c': 300}


def Sumall(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)

    return final


print("Sum :", Sumall(dict))

'''
Write a Python program to remove a key from a dictionary.
D = {'a':1,'b':2,'c':3,'d':4}
'''

myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(myDict)
if 'a' in myDict:
    del myDict['a']
print(myDict)

'''
Write a Python program to sort a dictionary by key
'''

myDict = {'ravi': 23, 'rajesh': 19,
          'sanjeev': 15, 'yash': 20, 'suraj': 32}

myKeys = list(myDict.keys())
myKeys.sort()
dict = {i: myDict[i] for i in myKeys}

print(dict)

'''
Write a Python program to remove duplicate values from  Dictionary.
'''

dic1 = {1: 1, 2: 2, 3: 2, 4: 3}
print("The original dictionary is:", dic1)
temp = []
res = {}
for key, val in dic1.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
print("The dictionary after removing the duplicates is:", res)

'''
Write a program to determine frequency of number in a list of numbers.
'''

random_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
frequency = {}

for item in random_list:
    if item in frequency:

        frequency[item] += 1
    else:

        frequency[item] = 1

print(frequency)
