
st = "hello world"

st = "Python"
print(st[:2], st[-2:], st[2:-1], st[::-1], sep="\n")

st = "PYTHON"
# del(st[0])
st = "Hello"
print(st, id(st))
st += " World"
print(st, id(st))

st = "welcome to the world of python"
print(st.capitalize())
print(st.upper())
str2 = st.title()
print(str2.swapcase())
st = "python"
print(st.ljust(50, '.'))
print(st.rjust(50, '-'))
print(st.center(50, '*'))
# encode
st = "PYTH" + "\u229a" + "N"
print(st)
print(st.encode(encoding="ascii", errors="namereplace"))
enc = st.encode(encoding="utf16", errors="namereplace")
print(enc)
main = enc.decode(encoding="utf16", errors="namereplace")
print(main)

pwd = "Kuldeep"
import hashlib

enc = hashlib.md5(pwd.encode(encoding="utf8"))
print(enc.hexdigest())

arr = ["https:\\www.gmail.com", "https:\\www.iitk.ac.in", "www.outlook.com", "www.nic.ac.in"]

for domain in arr:
    if (domain.startswith("https")):
        print(domain)

st = "hello world"
print(st.find("l", 5))

age = 35
name = "King"
print("my name is " + name + " and i am " + str(age) + " years old")
print("my name is %s and i am %d years old " % (name, age))
print("my name is {} and i am {} years old ".format(name, age))
print(f"my name is {name} and i am {age} years old ")
st = "hello"
# print(st.index("z"))
# print(st.find("z"))

import string

print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.hexdigits)
print(string.printable)
print(string.punctuation)
st = "python is a high level language"
vov = "aeiou"
rep = "12345"
ttab = str.maketrans(vov, rep)
print(ttab)
print(st.translate(ttab))

import string

st = "python is a high level language"

main = string.ascii_lowercase
mask = main[::-1]
ttab = str.maketrans(main, mask)

stext = st.translate(ttab)
print(stext)
print(stext.translate(str.maketrans(mask, main)))
lst = ["noida", "dehradun", "kanpur", "mumbai", "manali"]
print(lst)
res = "-".join(lst)
print(res)
main = res.split("-")
print(main)
pno = input("enter ur phone no")
if (len(pno) == 10 and pno.isdigit()):
    print("valid pno")
else:
    print("invalid pno")

st = "hello"
print(st.upper())
print(str.upper(st))

st = "hello world"
st = st.upper()
print(st.count("L"))
print("hello world".upper().count("L"))
