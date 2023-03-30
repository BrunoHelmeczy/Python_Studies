# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

def writeWeSeeTrees(word = 'tweesers '):
    out = word[1:3] + word[-1] + word[4:1:-1] + word[-1] + word[0] + word[6] + word[2:4] + word[-2]
    return out
