# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet_many(greeting: str = 'Hello', **kwargs):
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

def write_letter(name: str, text: str = 'Lovely to meet you'):
    greeting = f"Hello {name}, {text} \n"
    goodbuy  = f"Good Buy {name}, it was {text}"
    return greeting + goodbuy


