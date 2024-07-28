# control flow
# if statements: executes a block of code if a condition is true e.g
 
import variables
if variables.x < 2:
 print(f'I got it right! {variables.a}')

# if- else statement executes one block of code if a condition is true other wise, executes another block
else:
 print(f'Not right! {variables.b}')

#  if-elif-statement executes different blocks of codes depending on multiple conditions

r=18
if r > 12:
 print('r is greater than 10')
elif r > 2:
 print('r is greater than 2 but not greater than 12' )
else:
 print('r is 10 or less')

score= int(input('please enter your score '))

if score >= 70:
 print('You passed with an A')
elif score >=60:
 print('You passed with a B')
elif score >= 50: 
 print('You passed with a C')
elif score >= 40:
 print('You passed with a D')
elif score >= 30:
 print('You passed with an E')
else:
 print('You failed this test- F')

 








 


