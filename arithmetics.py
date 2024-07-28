# This file is to demonstrate arithmetic operations in python

x = 2
y = 4

i = 1.5
j = 0.2

# addition
sum = x + y
print(f"First addition is: {sum}")
sum1 = x + i
sum2 = x + j
print(f"Addition is: {sum1}")
print(f"Second Addition is: {sum2}")

# subtract
minus = y - x
minus1 = y - i 
minus2 = y - j
print(f"Subtraction is: {minus}")
print(f"Second Subtraction is: {minus1}")
print(f"Third Subtraction is: {minus2}")

# multiply
mul = i * j
mul1 = x * y
print(f"Multiplication is: {mul}")
print(f"Second multiplication is: {mul1}")

#division
div1 = i / j
div2 = x / y 
print(f"Division is: {div1}")
print(f"Second division is: {div2}")

# floor division
floor1 = x//i
floor2 = i//j

print(f"floor division is: {floor1}")
print(f"Second floor division is: {floor2}")

# Modulus
mod = x % y
mod1 = i%j
print(f"modulus is: {mod}")
print(f"modulus is: {mod1}")

# exponential
exp1 = x**j
exp2 = i**x
print(f"Exponential is: {exp1}")
print(f"Second exponential is: {exp2}")

# Operation precedence
# 1. Parentheses
t=2
u=4
v=6
op1= t + u * v
print(f"operation1 is: {op1}")
op2= (t + u) * v
print(f"operation2 is: {op2}")