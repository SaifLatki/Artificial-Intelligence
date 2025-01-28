
num=int(input("Enter the number of elements in the list:"))
total=0
for i in range(num):
    element=int(input(f'Enter the element {i+1} :'))
    total+=element
    
print(f'The sum of the numbers is: {total}')