# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."

def extractKeyWord(keyword = 'buttercup', text = s):
    index = s.find(keyword)

    if (index == -1):
        return None
    else:
        return s[index:(index + len(keyword))]
    
Keywords = ['flour', 'grapple', 'leggin', 'buttercup', '   ']
[extractKeyWord(x) for x in Keywords]
