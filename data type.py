'''
variable creation...
'''

var1 = 100
print(var1)

'''
type of created variable can be done by type function...
'''

print(type(var1))

'''
to convert number in binary 
'''
num = 0b0101
print(num)

'''
to use octal number use 0o
'''
num = 0o121
print(num)


'''
ox to get hexadecimal number..
'''
num = 0xA
print(num)

'''
for string also we can find...
'''
num = 0xFACE
print(num)

'''
to use exponential of 10 use e2
'''
num = 2e2
print(num)

'''
complex number can also be stored
'''
num = 12+5j
print(num)

'''
to get real part of a given complex number..
'''
print(num.real)

'''
to get conjugate of a complex number use conjugate() ...
'''
print(num.conjugate())

'''
to get two imaginary part of two complex numbers...
'''
num2 = 12 + 6j
sum = num + num2
print(sum)

'''
boolean number
'''
gra = True
print(gra)

print(type(gra))

'''
convert to strings ...
'''
num1 = 10
num2 = '10'
print(str(num1) + num2)

'''
use eval() to evaluate given python expression...
'''
bond = 123
print(eval('bond'))

'''
evaluate the python expression...
'''
print(eval("123*34+56-78/4" ))

'''
program to sum two numbers
'''
num1 = int(input("Enter the 1st Number: "))
num2 = int(input("Enter the 2nd Number: "))
num3 = num1+num2
print("Output=",num3)


'''
function usage of def
'''
n1 = int(input("Number 1:"))
n2 = int(input("Number 2:"))
def add(n1,n2):
    sum1 = n1 + n2
    return sum1
print("Sum is: ",add(n1,n2))


'''
for subtraction of two numbers...
'''
def sub(n1,n2):
    return n1 - n2
print("Subtraction: ",sub(n1,n2))


'''
for multiplication of two numbers...
'''
def multiply(n1,n2):
    return n1*n2
print("Multiplication: ",multiply(n1,n2))



'''
Division of two numbers..
'''
def div(n1,n2):
    return n1//n2
print("Division: ",div(n1,n2))


'''
return none when return not mentioned..
'''
val1 = 10
val2 = 23
def add2(val1,val2):
    val1 + val2
res = add2(val1,val2)
print("res = ",res)


