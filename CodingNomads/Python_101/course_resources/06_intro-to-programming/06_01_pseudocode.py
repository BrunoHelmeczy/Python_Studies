# Your cat just had kittens! Now you want to put up an ad to give them
# to your friends. You'll need to save all names of the kittens,
# confirm that they each of them is cute, and show a message that
# that kitten is ready for adoption.
#
# Break this task up into a couple of steps of pseudocode
# and write the pseudocode below in code comments.
# You don't need to write any functional code, just map out the steps.
kittens = ['alma', 'babe', 'cutie', 'damnpretty', 'extremelysexy']
cutes = [True, False, True, True, False]

for kit in kittens:
    Ind = kittens.index(kit)

    if cutes[Ind]:
        print(kit.capitalize() + ' is Cute an Ready for adoption')
    else:
        print(kit.capitalize() + ' is not yet Cute enough and Ready for adoption')


