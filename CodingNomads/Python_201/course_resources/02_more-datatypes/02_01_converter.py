# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"
chk1 = tuple([w for w in string])

[w for w in chk1]

chk1.count('o')
chk1.index('o')

chk = (1, 2, 3, 4)

chk.count(2)
chk.index(2)


import urllib.request as req
from itertools import compress

def getHangmanWords():
    word_site = 'https://www.mit.edu/~ecprice/wordlist.10000'
    Words = req.urlopen(word_site).read().decode('utf-8').replace('\n', ' ').split(' ')
    return list(compress(Words, [len(word) >= 5 for word in Words]))

Words = tuple(getHangmanWords())
sorted(set([w[len(w) -1] for w in Words]))
sorted(set([w[-1] for w in Words]))

chk = ['a', 1]

type(chk[0])


a = [1, 2, 3]
b = a
c = a.copy()

b[0] = 123
a[1] = 1234

c
b
a.append(4) # append by value after end
a.insert(2, 934)
a.index(934)

a.sort()

a + b

a.pop(0) # remove by index
a.remove(4) # remove by value

chk = {'a': 'a','b': 'aa','c': 'aaa', 'd': 'aaaa', 'e': 'aaaaa' , 'f':{'fa':'aaaaaa_a'}}

type(chk.items())
list(chk.values())
list(chk.keys())

type(chk)
type(chk['f'])
type(chk['f']['fa'])
chk['g'] = {'ga': 'aaaaaaa_a'}

[k for k in chk]
[k for k in chk.keys()]
[v for v in chk.values()]
[(k, value) for (k, value) in chk.items()]

x = 1, 2
x = tuple()
x = ()

x = [1, 2, 3]

x.insert(3, 4)
x.append(5)
x += [6, 7]
x.extend([8, 9])

y = {}
y[1] = 'b'

