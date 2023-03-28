
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

def ceasarCypher(secret, cipher = -1):
    TrueCypher = cipher % 26
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz" * 2
    out = ''

    for w in secret:
        if w.lower() not in lowercase_letters:
            # not a letter --> return same character
            out += w
        elif w != w.lower():
            # capital letter --> cypher & return .upper()
            index = lowercase_letters.find(w.lower())
            out += lowercase_letters[index + TrueCypher].upper()

        else:
            # return cyphered letter 
            index = lowercase_letters.find(w)
            out += lowercase_letters[index + TrueCypher]
    return out


for i in range(-25, 27):
    ceasarCypher(secret = secret, cipher = i)

solution = ceasarCypher(secret = secret, cipher = 7)
