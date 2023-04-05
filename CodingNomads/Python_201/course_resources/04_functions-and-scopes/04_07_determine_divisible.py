# Write a script where you complete the following tasks:
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def divisibleBy4and7(nr: int = 1000000):
    return nr % 4 == 0 and nr % 7 == 0

def divisibleBy4or7(nr: int = 1000000):
    return nr % 4 == 0 or nr % 7 == 0

def checkdiv(Nr: int):
    print(f"Is {Nr} divisible either by 4 or 7 ? Answer: {divisibleBy4or7(Nr)}")
    print(f"Is {Nr} divisible either by 4 and 7 ? Answer: {divisibleBy4and7(Nr)}")

checkdiv(1023488)