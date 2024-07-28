#control flow statements 
# Break statement
for i in range (10):
 if i == 5:
  break
 print(i)
#continue statement
for i in range(10):
 if i % 2 == 0:
  continue
 print(i)

 #pass statement
 for i in range(10):
    if i % 2 == 0:
        pass  # Placeholder for future code
    print(i)

# Nested control flow
x = 20
if x > 10:
    print("x is greater than 10")
    if x > 15:
        print("x is also greater than 15")
# nested loops
for a in range (4):
 for b in range (3):
  print(f" a = {a}, b ={b}")