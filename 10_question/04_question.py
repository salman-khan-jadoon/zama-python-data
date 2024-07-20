# Write a Python program that takes a year as input and checks if it is a leap year
year =int(input("enter a leap year:"))
if year % 4 ==0:
    print(f"{year} is leap year")
elif year % 100 == 0:
    print(f"{year} is not leap year")
elif year % 400 == 0:
    print(f"{year} is  leap year")
 