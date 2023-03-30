# Write the necessary code to print the BIG PYTHON string shown below.
# Research multi-line strings to make this easier for you :)
    # 5      12 15 18 21  25  29 32   37   424446  50      58
    # PPPP   Y     Y  TTTTTTTTT  H    H      O     N       N
    # P   P   Y   Y       T      H    H     O O    N N     N
    # P   P    Y Y        T      H    H    O   O   N  N    N
    # PPPP      Y         T      HHHHHH    O   O   N   N   N
    # P         Y         T      H    H    O   O   N    N  N
    # P         Y         T      H    H     O O    N     N N
    # P         Y         T      H    H      O     N       N


def GenerateBigPython():
    print('P')

    'P'*4 + ' '*3 + 'Y' + ' '*5 + 'Y' + ' '*2 + 'T'*9 + ' '*2 + 'H' + ' '*4 + 'H' + ' '*4 + 'O' + ' '*4 + 'N' +' '*7 + 'N'

    repr('P')