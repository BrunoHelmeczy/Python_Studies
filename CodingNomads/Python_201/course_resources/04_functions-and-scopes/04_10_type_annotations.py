# Add type annotations to the three functions shown below.

def multiply(num1: float, num2: float):
    return num1 * num2

def greet(greeting: str, name: str):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def shopping_list(*args: any):
    [print(f"* {item}") for item in args]
    return args
