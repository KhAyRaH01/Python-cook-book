# functions are reusable block codes that perform a specifc task and is defined by 'def" keyword
# functions can take arguments and return values

def greet(name):
    print(f"Hello, {name}!")
# calling function
greet("Abike")

# returning values
def add(x, y):
    return x+y

result= add(2,4)
print(result)

def multiply(a, b):
    return a * b

result= multiply(2,5)
print(result)  

# variable-length arguments

def add(*args):
    return sum(args)

result = add(1, 2, 4, 8, 9)
print(result)

# using default arguments

def multiply(a=1, b=1):
    """
    This function takes two arguments and returns their product.
    If no arguments are provided, it defaults to multiplying 1 by 1.
    
    Parameters:
    a (int or float): The first number. Default is 1.
    b (int or float): The second number. Default is 1.
    
    Returns:
    int or float: The product of a and b.
    """
    return a * b

# Calling the multiply function without arguments
default_result = multiply()
print(default_result)  # Output: 1

# Calling the multiply function with one argument
partial_result = multiply(5)
print(partial_result)  # Output: 5

# Calling the multiply function with two arguments
full_result = multiply(5, 3)
print(full_result)  # Output: 15

    
