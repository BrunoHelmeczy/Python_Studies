# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.
def countVowels(string = 'hello hello hellooooo'):
    return [string.count(x) for x in ['a', 'e', 'i', 'o', 'u']]

countVowels(string = 'hi my name is bruno im 29 years old and i just got laid off by SAP and fuck them becasue what the fuck')