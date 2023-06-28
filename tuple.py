lst = [12, 23, 34, 45]
tup = tuple(lst)
print(tup, type(tup))
tup = ('t', 'a', 'r', 'a')
print(tup, type(tup))
tup = ("james", "king", "blake")
# tup[0]="blake"


tup = (10, 20, 30, 40, 50)
print(tup[0], tup[-1])
print(tup[:2], tup[-2:], tup[::-1])

tup = (12, 12.4, True, "jame", 12 + 7j, [12, 23, 34])
for i in tup:
    print(i, type(i))

tup = (12, 13, 14, [100, 200])
tup[-1].append(300)
print(tup)

tup = 123,
print(tup, type(tup))

vals = 12, 23, 34, 45
print(vals)
a, *b = vals
print(a, b)

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
print(f"Before swaping num1={num1}  num2={num2}")
num1, num2 = num2, num1
print(f"After swaping num1={num1}  num2={num2}")

num1 = 0
num2 = 1
print(num1, num2, end=" ")
for i in range(8):
    num3 = num1 + num2
    print(num3, end=" ")
    num1 = num2
    num2 = num3

num1, num2 = 0, 1
for i in range(10):
    print(num1, end=" ")
    num1, num2 = num2, num1 + num2

tup = (12, 23, 34, 12, 45, (12, 23, 23, 34))
print(tup.count(12))
print(tup.index(12, 2))


"""
importing dis
"""
import dis


def lstfun():
    lst = [10, 20, 30, 40, 50, 60]


def tupfun():
    tup = (10, 20, 30, 40, 50, 60)


dis.dis(lstfun)
dis.dis(tupfun)

"""
to load a tuple we require less instructions
"""