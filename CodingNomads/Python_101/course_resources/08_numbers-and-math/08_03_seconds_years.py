# Move the code you previously wrote to calculate
# how many seconds are in a year into this file.
# Then execute it as a script and print the output to your console.

import os

path = 'CodingNomads/Python_101/course_resources/05_machine-setup/'
File = os.listdir(path)[0]

fullName = path + File

os.system('py ' + fullName)
