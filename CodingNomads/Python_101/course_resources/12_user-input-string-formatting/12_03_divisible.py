# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

# divisibility rules
# 2 --> last digit div by 2
# 3 --> sum of digits divisibly by 3
# 4 --> last 2 digits div by 4
# 5 --> last digit div by 5
# 6 --> div by 3 & div by 2
# 7 --> ???
# 8 --> last 3 digits divisible by 8
# 9 --> sum of digits divisible by 9
# 10 --> last digit == 0
# 11 --> sum(even placed digits) - sum(odd placed digits) divisible by 11 
# 12 --> div 4 & div 3
# 13 --> ???

def checkDivisibility(Nr = 102, divisor = 3):
    implemented = [2, 3, 4, 5, 6, 10]
    nr = str(Nr)
    if divisor not in implemented:
        print(f"Divisibility check for {divisor} not available. Please pick from: {implemented}")
        return None
    elif Nr > 1000000000 or Nr < 1:
        print(f"{Nr} is out of range. Pick Numbers between 1 - 1billion")
        return None
    elif divisor in [2, 5, 10]:
        return ((int(nr[len(nr) - 1 ]) % divisor) == 0)    
    elif divisor == 3:
        return ((sum([int(x) for x in nr]) % divisor) == 0)
    elif divisor == 4:
        return ((int(nr[(len(nr) - 2):]) % divisor) == 0)
    elif divisor == 6:
        return (checkDivisibility(Nr, 2) and checkDivisibility(Nr, 3))
    
# checkDivisibility(102, 2)
# checkDivisibility(102, 3)
# checkDivisibility(102, 4)
# checkDivisibility(102, 5)
# checkDivisibility(102, 6)
# checkDivisibility(102, 10)