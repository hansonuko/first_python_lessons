myint = 7
print(myint)
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

myfloat = float(20)
print(myfloat)

mystring = 'Hello'
print(mystring)
mystring = "Uko Hanson"
print(mystring)

mystring = "Don't worry about apostrophe"
print(mystring)

one = 1
two = 2
three = one + two
print(three)
four = three + 2
print(four)

print('Dont\'t worry about food')
print('Don\'t worry about (food)')
print("Take me to a\nnew line")
print(r"Don't take me to a \new line")  # use double quotes where you have to use an apostrophe.

hello = "hello"
world = "world"
helloworld = "hello" + "world"
print(helloworld)

a, b = 3, 4
print(a, b)

mystring1 = "hanson"
myfloat1 = 15.0
myint1 = 17

if mystring1 == "hanson":
    print("String is %s" % mystring1)
if isinstance(myfloat1, float) and myfloat1 == 15.0:
    print("Float is: %.2f" % myfloat1)
if isinstance(myint1, int) and myint1 == 17:
    print("Integer is %d" % myint1)