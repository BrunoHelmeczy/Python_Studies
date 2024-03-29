# 1) 7 to the power of 4 ?
ans1 = 7 ** 4

# 2) split string
string = "Hi there Sam!"
ans2 = string.split(' ')

# 3) 
planet = 'Earth'
diameter = 12742

ans3 = f"The {planet}'s diameter is {diameter} kms"

# 4) nested list --> grab hello
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

ans4 = lst[3][1][2][0]

# +1) Unnest arbitrarily deeply nested list
lst2 = [[1, 2, 3],[1, 2, 3],[1, 2, 3]]
# [item for sublist in lst2 for item in sublist]

def flatten(lst):
    out = []

    [out.extend(sub) if isinstance(sub, list) else out.append(sub) for sub in lst]

    if max([isinstance(sub, list) for sub in out]):
        return flatten(out)
    else:
        return out

flatten(lst2)
flatten(lst)

# 5) grab hello fr nested dict()
dic = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

ans5 = dic['k1'][3]['tricky'][3]['target'][3]

# 6) grab domain name from email
email1 = "user@domain.com"
email2 = "helmeczybruno32@gmail.com"

def getEmailDomain(email_string):
    return email_string.split("@")[1]

getEmailDomain(email1)
getEmailDomain(email2)

# 7) f(x) to find term dog in input string
import re
longstring = "this is a long string containing the word dog'go"

def findDog(input_string):
    return re.sub('[^\w]', '', input_string.lower()).find('dog') != -1

findDog(longstring)
findDog('this is another bloody string with cat')

# 8) count number of times dog appears in string
longstring2 = "this is a long string containing the word dog'go. who's a good boi dog'go"

def countDogs(input_string):
    base_str = re.sub('[^\w]', '', input_string.lower())

    return len(re.findall('dog', base_str))

countDogs(longstring2)
countDogs('this is a random string')

# 9) lambda expr + filter() to startwith('s')
seq = ['soup','dog','salad','cat','great']

ans91 = list(filter(lambda x: x.startswith('s'), seq))
ans92 = [x for x in seq if x.startswith('s')]

# 10) f(x) caught_speeding()
# isBirthday = True
def caught_speeding(speed: int, isBirthday: bool):
    Speed = speed - 5 * isBirthday

    if Speed <= 60:
        return 'No ticket'
    elif Speed <= 80:
        return 'Small ticket'
    else:
        return 'Big ticket' 

# caught_speeding(60, False)
# caught_speeding(61, False)
# caught_speeding(70, False)
# caught_speeding(85, True)
# caught_speeding(86, True)


