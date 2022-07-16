from cmath import pi
from gettext import install
from math import radians


print('hello world')

# 1) Basics ----
# 1.1) Vars & Types ----
height = 1.83
weight = 121.5

bmi = weight/(height**2)

name = 'bruno'
lastname = 'helmeczy'
age = 28
handsome = True

type(bmi) # float
type(name) # str
type(lastname)
type(age) # int
type(handsome) # bool

# Addition by type
    # float / int --> add
age + height
weight + height

str(age)
float(age)
int(weight) # not rounding --> removes decimal figures
round(weight)

    # str-s --> append strings
name + lastname

    # bool --> True = 1 / False = 0
int(True)
int(False)

# Ex 3-4)
mymoney = 100
interestearnings = mymoney * 1.1 ** 7
print("I started w $", str(mymoney)," bucks & now have $",str(round(interestearnings,2)))

pi_str = "3.1415926"
float(pi_str)

# 2) Lists  ----
heights = [1.80, 1.66, 1.79, 1.83, 1.60, 1.62]
namesheights = ['dad', 1.80,'mom',  1.66, 'ubi',  1.79, 'buda', 1.83, 'frutti',  1.60, 'pofi',  1.62]
namesheights2 = [['dad', 1.80], ['mom', 1.66], ['ubi', 1.79], ['buda', 1.83], ['frutti', 1.60], ['pofi', 1.62]]

type(heights)
type(namesheights)
type(namesheights2)

# Ex 1-3 ---
a = 31
b = 43
c = 95
d = 25
e = 2394
mylist = [a, b, c, d, e]
[1+2, 'a' * 5, 3]

    # Subsetting
heights[0]   # --> 1st element
heights[0:3] # --> 1st to 3rd element
heights[:4]  # --> up to 4th element
heights[1:]  # --> starting from 2nd element
heights[-1]  # --> get last element 
heights[-2]  # --> get 2nd to last element 

namesheights2[2][1]
namesheights2[2:4][1]

    # List manipulation
namesheights[7] = 1.81
namesheights[8:10] = ['fruzsina', 1.59]
namesheightsall = namesheights + ['mark', 1.2, 'lena', 1.65]
del(namesheightsall[12:])
namesheightsall

x = ['a', 'b', 'c']
y = x
    # values are updated by reference --> i.e. a lá data.table 
    # --> copy() method / [:] slicing to list all elements explicitly / wrap in list()
x[2] = 'bla'
z = y.copy()
z[2] = 'c'

a = x[:]
a[2] = 'c'

x
y
z
a

# +1: ; sign 4 1+ commands on 1 line:
mylist = list(range(1,10)) ; print(mylist[:5])

# subsetting from end
mylist[-4:-2]

# 3) Functions & Packages ----

# 3.1) Functions -----
type(mylist)
max(mylist)

round(float(heights[1]), 0) # either subset 1 element
round(heights, 1) # cant handle / comprehend lists directly

roundedheights = [round(x, 1) for x in heights] # Use List Comprehension instead

len(roundedheights) # Nr. elements in list

help(pow) # check documentation
pow(10, 3)  # Base, Exponent
pow(10, 3, 3) # Base, Exponent, Mod --> get remained fr integer division

sorted(heights) # sort Nr.s ascending by default
sorted(heights, reverse = True) # sort descending order

# 3.2) Methods -----
namesheights.index('ubi') 
namesheights2.index('ubi') # Not on list-of-lists

namesheights.count(1.81) 

names = ['dad', 'mom', 'ubi', 'buda', 'frutti', 'pofi']
names.reverse()

names[0].capitalize()
names[0].upper()
names[0].lower()
names[0].count('d')
names[0].replace('a', 'AAAAAA')

[x.capitalize() for x in names]             # w list comprehension
[x.replace('a', 'AAAAAA') for x in names]   # w list comprehension

names.append(['lena', 'mark']) #  adds nested list --> add 1 by 1 --> list comprehension
[names.append(x) for x in ['lena', 'mark']]

# 3.3) Packages -----
    # pip install numpy np --> run on Command Prompt
import sys
print(sys.version)
import numpy as np

npheights = np.array(heights)
type(npheights)



# 4) NumPy ----

