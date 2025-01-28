def personAge(age):
    if age<13:
        return "child"
    elif age >=13 and age<20:
        return "teenager"
    elif age>=20:
        return "adult"
    else:   
        return "invalid age"
    
age=int(input("Enter your age: "))
print(f'You are a {personAge(age)}')