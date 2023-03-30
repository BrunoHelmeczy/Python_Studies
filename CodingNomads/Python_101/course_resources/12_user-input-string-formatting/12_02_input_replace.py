# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please
def hideLettersInString(symbol = '$', string = 'more python programming please', index = 1):
    if len(string) < (index - 1):
        print(f"index {index} out of range. Input string is only {len(string)} characters long.")
        return None
    return string.replace(string[index - 1], symbol)
     

hideLettersInString(index = 2)