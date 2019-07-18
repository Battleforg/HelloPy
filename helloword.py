import random
print("Hello, World")
if 5 > 2:
    print("Five is greater than two")

x = 5
y = "Hello World"
string2 = 'String2'

# some comments

"""T
this is a multiline string or comment
It is ignored by Python
"""

# assign Value to Multiple Variables
x, y, z = 'Orange', 'Banana', 'Cherry'
print(x)
print(y)
print(z)
print(x + z)
# Rumtime TypeError: unsupported operand type(s)
# print(1 + z)
print(1 + 2)

# int
x = 1
# float
y = 2.9
# complex
z = 1j
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

# 2
a = int(y)
# 1.0
b = float(x)
print(a)
print(b)
print(type(a))
print(type(b))

print(random.randrange(1, 10))

# multiline string: """ .... """ or ''' ... '''
templateString = "I want {2} sdfdf of sfsf {1} for {0}"
# the number of arguments needs to match the number of placeholders
print(templateString.format(x, y, z))
# floor division // rounds the result down to the nearest whole number
print(15 // 2)
# exponentiation
print(2 ** 3)
# corresponding assigment operators //= **=

# List ordered, changeable, allow duplicate
aList = [1, 2, 3]
print(aList)
print(aList[1])  # 2
aList[2] = 5
print(aList[2])  # 5
print(aList)
# alist[3] = 5  index out of range

# Tuple ordered, unchangeable
aTuple = (1, 2, 3)
print(aTuple)
print(aTuple[2])

# Set unordered, unindexed, cannot change but can add or remove()
aSet = {"apple", "banana", "cherry"}
print(aSet)
for x in aSet:
    print(x)

# add one item
aSet.add(1)
print(aSet)

# add mulitple items
aSet.update([1.2, 3.4, 3j, 9.9])
print(aSet)

# dictionary unordered, changable, indexed