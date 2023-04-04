# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.
import pathlib

txt = pathlib.Path().resolve().joinpath('CodingNomads/Python_201/course_resources/03_file-input-output')

with txt.joinpath('words.txt').open('r') as Input:
    text = Input.read()
    words = text.split('\n')
    out = '\n'.join([w for w in reversed(words)])

with txt.joinpath('words_reverse.txt').open('a') as Output:
    Output.write(out)

