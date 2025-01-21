
# Create a variable named carname and assign the value Audi to it.
carname="Audi"


# Create a variable named x and assign the value 30 to it.
x=30

# Display the sum of 5 and 15, using two variables
# Create a variable called z, assign x + y to it, and display the result.
x=5
y=15
z=x+y
print(z)

# Remove the illegal characters in the variable name:
# 2my-first_name = "John“ #incorrect variable name
my_first_name = "John" #correct variable name

# Assign the same value to three variables in one code line.
n1=n2=n3=2

# Define same name to local and global variable and display its different 
# values
def myfunc():
  global x
  x = 34
  print(x)

myfunc()
print(x)