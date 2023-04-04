# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.
import pathlib
txt = pathlib.Path().resolve().joinpath('CodingNomads/Python_201/course_resources/03_file-input-output/words.txt')

# Input = txt.open('r')
with txt.open('r') as Input:
    text = Input.read()
    words = text.split('\n')
    Words = [x for x in filter(lambda x: len(x) > 0, words )]

    Lens = [len(x) for x in Words]

    Min = min(Lens)
    Max = max(Lens)

    MinWords = [w for w in filter(lambda x: len(x) == Min, Words)]
    MaxWords = [w for w in filter(lambda x: len(x) == Max, Words)]

    print(f"The shortest word(s) are {Min} characters long; the longest are {Max}.")
    print(f"There are in total {len(Words)} words.")
    print(f"These are the shortest word(s): {MinWords} ")
    print(f"These are the longest  word(s): {MaxWords} ")
