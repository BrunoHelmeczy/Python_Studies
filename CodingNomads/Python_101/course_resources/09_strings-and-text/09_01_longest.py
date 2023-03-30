# Which of the following strings is the longest?
# Use the len() function to find out.

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

words = [
    longest_german_word
    , longest_hungarian_word
    , longest_finnish_word
    , strong_password
]

lens = [len(w) for w in words]

LongestWord = words[lens.index(max(lens))]
print(LongestWord)

LongestWord[0:10]
LongestWord[0]
LongestWord[9]
LongestWord[-1]

s = 'plumage'
s[::-1]

s = s + '24'