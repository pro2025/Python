'''
types of operators
-arithmetic operators i.e + - * / % ** //
'''
num1 = int(input("enter the number1:"))
num2 = int(input("enter the number2:"))
print("Sum= ",num1 + num2)
print("Sub= ",num1 - num2)
print("pro= ",num1 * num2)
print("Div= ",num1 / num2)
print("FDiv= ",num1 // num2)
print("Mod= ",num1 ** num2)


'''
arithmatic operators on string 
'''
print("Hello"+"World")
print("Hello" * 4)


'''
assignment operator
=
+=
-=
*=
/=
%=
//=
**=
'''
var = 100
print(++var)
var+=1
print(var)


'''
comparison operator
== , != ,> ,< ,<= ,>=
'''
num1 = 10
num2 = 20
num3 = 30
print(num1 == num2)
print(num1 <= num2)
print( num1 < num2 < num3)

'''
logical operator
and , or , not
and gives true if both the operands are true
or gives true if either of the operands is true 
not gives true if operand is false 
'''
if num1 > num2 and num2 > num3:
    print("The numbers are greater than ",num1)
if num1 > 0 and num2 >0 and num3 > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")


'''
identity operator
is - the result becomes true if values on either side of the operator points to the same object and false otherwise
is not - the result becomes false if the variables on either side of the operator points to the same object

'''
print(id(num1))
num4 = num1
print(num1 is num4)
print(num1 is num3)

'''
membership operators
in - true if value/variable is found in the sequence
not in - true if value/variable is not found in the sequence
'''
print("A" in "AEIOU")
print("" in "AEIOU")
print(23 in [12,23,34,45,55])
print(23 not in [12,23,34,45,55])

b1 = 1
b2 = 0
print(b1|b2)
print(b1 and b2)
print(b1 ^ b2)



'''
using ~ compliment operator which give negative of given value
'''
print(~12)
'''
12 in bit is 00001100
1 will become 0 
0 will become 1
so it will become 1111001 which is 13 
~ to convert a number and store in negative form
'''
print(10 + (~5+1))
print(12 << 1)
print(12 >> 1)

'''
00001100 << 00000001
'''

'''
preference operators
'''
exp = 12+4*5
print(exp)
exp1 = 12*4/2
print(exp1)
exp2 = 12/4*2
print(exp2)
res = 2**3**2
print(res)

'''
operators with the same precedence are evaluated from left to right
'''




