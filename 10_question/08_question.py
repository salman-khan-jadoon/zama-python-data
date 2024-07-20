# Write a Python program that takes a single character as input and checks if it is a vowel (a, e, i, o, u) or a consonant. 
character =input("enter the character number :")
if character .lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f"{character} is vowal .")
else :
    print(f"{character} is consonant .")