#   comprehension  concise way to create lists, dictionaries, and sets using 
# basic list comprehension

fruits= ['apple', 
         'pineapple', 
         'orange', 
         'cranberry', 
         'bluberry', 
         'date', 
         'guava',
         'banana']

uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)
fruit_length= [len(fruit) for fruit in fruits]
print(f'fruit lengths: {fruit_length}')

# list comprhension with a condition
long_fruits_names= [fruit for fruit in fruits if len(fruit) >= 6]
print(f"The long fruits are: {long_fruits_names}")

uppercased_long_fruits= [fruit.upper() for fruit in fruits if len(fruit)>=6]
print(f"uppercased long fruits are: {uppercased_long_fruits}")
 
 
# list comprehension with transformation and condition
b_fruit_lenghts= [len(fruit) for fruit in fruits if fruit.startswith('b')]
print(f'the lenths of fruits that starts with b are: {b_fruit_lenghts}')

# nested list comprehension
birds=[['pigeon', 'duck'], ['peacock', 'canary']]
flattened_birds= [bird for sublist in birds for bird in sublist]
print(f'this is a flattened bird list: {flattened_birds}')

squares=[x**2 for x in range(10)]
print(f'squares: {squares}')

# Dictionary comprehension

animals=['lion', 'tiger', 'giraffe', 'cobra', 'python', 'shark', 'whale']
# basic dictionary comprehansiom
animal_length={animal: len(animal) for animal in animals}
print(f'animal lengths are: {animal_length}')
# converting list to dictionary and turning into capital letter
animal_upper= {animal.upper() for animal in animals}
print(f'animal upper are: {animal_upper}')
# dictionary comprehension with condition
animal_length={animal: len(animal) for animal in animals if len(animal) > 5}
print(f'animal lengths greater than 5 are: {animal_length}')

# set comprehension
first_letters={animal[0] for animal in animals}
print(f'first letters of animals are: {first_letters}')