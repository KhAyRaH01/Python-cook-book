# This file is to demonstrate variables
#Integers
x = 6
print(x)
#string
y = 'Ade' 
print(y)
#float
z = 2.989
print(z)
# Boolean
a = True
b = False
print(a)
print(b)
# list
fruits =[
    'apple',
    'pineapple',
    'guava',
    'watermelon'
]

print(f'List of fruits are {fruits}')

# tuple
d = (
    'shopping',
    3000, 
    'Hotel'
    )

print(d)
# dictionary: has key and values both can be any type, 
e = {
    'Name': 'Ade', 
    'Phone_no': '08025635532', 
    'School' : 'LASU',
    'City' : 'Lagos'
    }

players = {
    1 : 'Ronaldo',
    2 : 'Messi',
}

print(players[1])

print (e['Name'])
print (e['School'])

# sets
f = {
    'Ade',
    'LASU',
    'Lagos',
    2000 
    }

print(f)

# Nonetype
g = None
print(g)

# Ranges A sequence of numbers, often used in loops.
h = range(1, 12, 2)
print(f'The ranges of numbers are {h}')

# frozen sets (immutable sets)
i = ([1, 2, 3, 4, 5])
print (f'An example of a frozen set is: {i}')

