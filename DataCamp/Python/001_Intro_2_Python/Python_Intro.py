from cmath import pi
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


# 3) Functions & Packages ----
# 4) NumPy ----
