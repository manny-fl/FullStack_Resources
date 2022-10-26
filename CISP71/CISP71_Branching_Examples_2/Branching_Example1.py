#reference https://www.w3schools.com/python/python_conditions.asp
#Python supports the usual logical conditions from mathematics:
#to comment more than one line high light the lines and press shift+alt+A
#to toggle comments Ctrl + / 

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b 

#If statment example 1
print("Example1")
print("=========")
a = 33
b = 200
if b > a:
  print("b is greater than a")
  

#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
# Other programming languages often use curly-brackets for this purpose.

####Elif
#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

#Example 2
print("Example2")
print("=========")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".
#*************************
#Else
#The else keyword catches anything which isn't caught by the preceding conditions.

#Example 3
print("Example3")
print("=========")
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  #commenting several lines
  """ In this example a is greater than b,
   so the first condition is not true, also the elif condition is not true,
   so we go to the else condition and print to screen that "a is greater than b".
  You can also have an else without the elif: """
  
  #Example 4
  print("Example 4")
  print("=======")
  #You can also have an else without the elif:

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
 
 #****** 
#Short Hand If
#If you have only one statement to execute, you can put it on the same line as the if statement.

print("Short hand if example 1")
print("===============")

#One line if statement:

if a > b: print("a is greater than b")

#Short Hand If ... Else
#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

print("Short hand if .. else Example")
print ("=========")
print("One line if else statement:")

a = 2
b = 330
print("A") if a > b else print("B")

#***Ternary operators
#This technique is known as Ternary Operators, or Conditional Expressions.
#You can also have multiple else statements on the same line:

print("Ternary operators- conditional expressions example")
print ("===========================================")

#Example
#One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#****the and keyword
#The and keyword is a logical operator, and is used to combine conditional statements:

#Example
print("Using and keyword - logical operator example")
print("============================================")
print("Test if a is greater than b, AND if c is greater than a:")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
  #***the or keyword
  #The or keyword is a logical operator, and is used to combine conditional statements:

print("Example using the or keyword - or logical operator")
print("=====================================================")
print("Test if a is greater than b, OR if a is greater than c:")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")