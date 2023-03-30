# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"

files = [file_1, file_2, file_3, file_4]

from itertools import compress
# files[x.endswith('pdf') for x in files] --> can't subset lists by condition natively ?!?!

pdfs = list(compress(files, [x.endswith('pdf') for x in files]))