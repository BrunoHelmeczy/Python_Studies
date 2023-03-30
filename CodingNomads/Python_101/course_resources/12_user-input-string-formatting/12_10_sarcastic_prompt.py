# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
def getFuzzyText(string = 'Create a sarcastic program that asks a user for their honest opinion'):
    out = [( string[x].lower() if (x % 2 == 0) else string[x].upper()) for x in range(len(string))]
    return ''.join(out)

getFuzzyText()