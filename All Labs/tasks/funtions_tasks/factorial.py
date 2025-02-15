def fact(n):
    f=1
    for i in range(1,n+1):
        
        f*=i
        
    return f

num=int(input("Enter the number for Factorial: "))
print(f'Factorial of {num} is: {fact(num)}')