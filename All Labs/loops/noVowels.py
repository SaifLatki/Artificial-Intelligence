words=input("Enter the words= ")

vowels=['a','e','i','o','u']
count=0

for i in range(len(words)):
    if words[i] in vowels:
        count=count+1

print(f'Number of vowels= {count}')