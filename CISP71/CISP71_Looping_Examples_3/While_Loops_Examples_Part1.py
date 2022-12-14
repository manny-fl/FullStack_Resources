#reference https://www.w3schools.com/python/python_while_loops.asp
#show them the following video https://www.youtube.com/watch?v=4dN4Cn4u2M0
# Python Loops
# Python has two primitive loop commands:
# while loops
# for loops
# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
print("Example 1 using while loop")
print("Print i as long as i is less than 6:")
print("remember to increment i, or else the loop will continue forever.")
print("========================================================")

i = 1
while i < 6:
  print(i)
  i += 1
  
#The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

print("Example 2: while loop using break")
print("===================================")
#With the break statement we can stop the loop even if the while condition is true:
print("Print i as long as i is less than 6:")
print("Exit the loop when i is 3:")

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
print("Example 3: while loop using continue statement")
print("================================================")
#With the continue statement we can stop the current iteration, and continue with the next:
print("Print i as long as i is less than 6:")
print("Continue to the next iteration if i is 3:")

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
  