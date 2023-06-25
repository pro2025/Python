"""
flow control
- if,if else,if elif,while,for,pass,break,continue
"""
"""
if , else if use..
"""
letter = "A"
if letter == "B":
    print("letter is B")
else:
    if letter == "C":
        print("letter is C")
    else:
        if letter == "A":
            print("letter is A")
        else:
            print("letter isn't  A,B and C")

"""
nested if and elif
"""
num = 10
if num > 5:
    print("Bigger than 5")
    if num <= 15:
        print("Between 5 and 15")

"""
loop functions..
"""
init = 1
while init <= 5:
    print(init, "Hello World")
    init += 1

while True:
    print("Hello World")
    ch = input("do u want to continue (y/n)")
    if ch != 'y':
        break
