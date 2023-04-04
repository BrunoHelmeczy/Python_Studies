# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).
import pathlib

txt = pathlib.Path().resolve().joinpath('CodingNomads/Python_201/course_resources/03_file-input-output/words.txt')

with txt.open('r') as Input:
    text = Input.read()
    words = text.split('\n')
    hide = [print(w) for w in words if len(w) > 20]
