# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class Ingredients:
    pass

i = Ingredients()
i.name = 'carrot'

class Ingredient:
    def __init__(self):
        self.name = 'carrot'


i = Ingredient()
i.name

class Ingredient:
    def __init__(self, name, quantity, origin):
        self.name = name
        self.quantity = quantity
        self.origin = origin

chk = Ingredient('pee', 3, 'Barbados')

chk.name
chk.origin
chk.quantity
