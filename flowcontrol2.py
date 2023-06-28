

"""
break statement is used to break out of a loop statement i.e stop the execution of a looping statement..
"""
x = 1
while True:
    print(x)
    x += 1
    if x == 3:
        break

"""
continue statement used to continue to next iteration of the loop..
"""
for x in range(6):
    if x == 3 or x == 6:
        continue
    print(x)


"""
pass statement used when a statement is required but program require no action..
want to leave python code as empty
"""
x = int(input("Input 1 or 2 or 3"))
while x == 1:
    if x == 1:
        print(" 1 python is a scripting language")
    elif x == 2:
        pass
    else:
        print("3 It is fun to learn Python")
    x += 1

for num in range(-1,-5,-1):
    print(num,end=" ,")

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break

if 4 + 5 == 10:
    print("True")
else:
    print("False")
print("True")


