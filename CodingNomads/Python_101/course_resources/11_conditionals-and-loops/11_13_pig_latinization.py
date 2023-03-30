# Fetch the text of the CodingNomads collaborative story from:
text = 'https://raw.githubusercontent.com/CodingNomads/collaborative-story/master/story.txt'
# Save it to a variable in this script and remember to use triple-double quotes
# for creating a multi-line string.
#
# Use a `for` loop to iterate over the story text
# and string slicing to translate it to ~pig latin.
# For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# You'll need to use conditional statements to decide when a word is over.
#
# For example: You would never guess --> ouyay ouldway evernay uessgay
import urllib.request
from itertools import compress

def translate2PigLatin(texturl = text):
    Text = urllib.request.urlopen(texturl).read().decode('utf-8')

    words = Text.replace('\n', '').split(' ')

    words2 = list(compress(words, [(len(w) > 0) for w in words]))

    piglatinwords = [(w[1:] + w[0] + "ay ") for w in words2]

    out = ''.join(piglatinwords)
    return out

solution = translate2PigLatin(text)


