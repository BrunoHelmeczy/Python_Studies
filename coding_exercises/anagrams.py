# blackrock exercise:
# given list of strings (words)
# find anagram of a string from remaining (earlier) items in list
# if anagram, then delete
# return list of strings without anagrams words in list (keep 1st version of anagram words)

words = ['blla', 'ball', 'frame', 'framer', 'gramm', 'mragm']
# exp_out = [True, False, True, True, True, False]

def filterAnagrams(stringlist):
    nested = [sorted(w) for w in stringlist]

    out_inds = [(nested[:i].count(nested[i - 1]) == 1) for i in range(1, len(stringlist) + 1)]

    return [stringlist[i] for i in range(len(stringlist)) if out_inds[i]]


filterAnagrams(words)

