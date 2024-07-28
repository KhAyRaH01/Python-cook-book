import variables
#  Loops ( for loop, while loop, )

# for loop iterates over a sequence like list, dict,tup or string e.g
for fruit in variables.fruits:
 print(f'List of fruits are: {fruit}')

#  while loop repeats a block of codes as long as a condition is true


 count=1
while count<10:
 print(f'count 1 starts here {count}')
 count +=1

#  Using 'break' in a while loop, this is used to exit a loop prematurely
count2= 0
while True: #The loop starts with while True, which creates an infinite loop.
 print(f'count 2 starts here:{count2}')
 count2 += 1  #The loop prints the current value of count and increments it by 1.
 if count2 == 10: #When count equals 5, the break statement is executed, which exits the loop.
  break
  
#   Using 'continue' in a while loop
count3= 0
while count3<20:
 count3 +=1
 if count3 % 2 == 0:
   continue
 print('this is count 3:', count3)

#  user input with a 'while loop
password = ""

while password != "secret":
 password = input("Enter the password: ")
else:

 print("Access granted!")

# Summing Numbers with a while Loop

n = 10    #Initialize n to the desired number of natural numbers to sum.
total = 0  ## total holds the running total of the sum
count = 1  #count starts at 1 and is incremented in each iteration of the loop

while count <= n:  # The loop runs as long as count is less than or equal to n
    total += count  #In each iteration, count is added to total, and count is incremented by 1.
    count += 1

print("Sum of first", n, "natural numbers is", total)
