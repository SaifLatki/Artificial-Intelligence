import calendar

def findleapYear(year):
    if calendar.isleap(year):
        return True
    else:
        return False

year = int(input("Enter the year: "))
if findleapYear(year):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year') 



