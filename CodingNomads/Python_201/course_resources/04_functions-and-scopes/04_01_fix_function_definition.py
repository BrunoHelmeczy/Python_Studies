# The following function definition has a whole lot of bugs in it!
# Run the script and follow Python's error hints to fix them all.
# After your fixes, the function should allow you to take a name as an input
# and return a greeting message that you can save to a variable.

def say_hello(name):
	return print(f"Hello {name}!")

greeting = hello(name)
print(greeting)

# args = ['bla', 'blabla']
def greet_many(greeting, *args):
	# """_summary_

	# Args:
	# 	greeting (_type_): _description_

	# Returns:
	# 	_type_: _description_
	# """    
    
    greetings = '\n'.join([f"{greeting}, {name}! How are you?" for name in args])
    return greetings

print(greet_many('Hello','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'))

# kwargs = {'george': 'IT', 'kate': 'architecture'}
def greet_many2(greeting: str = 'Hello', **kwargs):
	"""
	Generates a greeting.

	Args:
		greeting (str): blabla
		kwargs: blablablablabla

	Returns:
		str: personalized greeting messages
	"""

	greetings = '\n'.join([f"{greeting} {k} from {v}!!!" for k, v in kwargs.items()])
	return greetings

help(greet_many2)

print(greet_many2( George = 'IT', Kate = 'Architecture', Bruno = 'Data'))
print(greet_many2('Hello', George = 'IT', Kate = 'Architecture', Bruno = 'Data'))

my_list = ["apple", "banana", "orange"]
obj1 = enumerate(my_list)
print(obj1)