# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

def write_letter(name: str, text: str = 'Lovely to meet you'):
    greeting = f"Hello {name}, {text} \n"
    goodbuy  = f"Good Buy {name}, it was {text}"
    return greeting + goodbuy

print(write_letter('Bruno'))