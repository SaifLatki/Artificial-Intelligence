exp=input("Enter the Experation: ")

for i in range(len(exp)):
    if exp[::-1] == exp[::]:
        print(f'{exp}:is a Palindrome')
        break
    else:
        print(f'{exp}: is not a palindrome')
        break