# Write a Python program that takes a person's weight (in kilograms) and height (in meters) as input and calculates their Body Mass Index (BMI).
weidht=float(input("enter your weight :"))
height=float(input("enter your height :"))
bmi = weidht /(height **2)
if bmi < 18.5:
    print(f"your bmi is{bmi:.2f}and you are underweight.")
elif bmi < 25:
    print(f"your bmi is{bmi:.2f}and you are normal weight.")
elif bmi < 30 :
    print(f"your bmi is{bmi:.2f}and you are overweight.")
else :
    print(f"your bmi is{bmi:.2f}and you are obese.")



