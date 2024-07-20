# Write a Python program that takes a person's age as input and classifies them into one of the following age 
years=int(input("emter an persons year :"))
if years >= 0 and years <= 12 :
    print("he is a child")
elif years >=13 and years <= 19 :
    print("he is a teenager")
elif years >=20 and years <= 64 :
    print("he is a adult")
else:
    print("he is a senior")