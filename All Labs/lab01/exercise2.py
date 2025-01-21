#  S= “ This is a university “
# Find the length of string 
# Replace university by college
# Convert lower case into upper case
# Display 2nd last character
# Return the string without any whitespace at the beginning or the end.
# Find the number of words in variable S

s="This is a university"
print(len(s))
print(s.replace("university","college"))
print(s.upper())
print(s[-2])
print(s.strip())
print(len(s.split()))
