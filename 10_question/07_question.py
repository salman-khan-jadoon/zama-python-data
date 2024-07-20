# Write a Python program that takes two numbers and an operator (+, -, *, /) as input and performs the corresponding arithmetic operation
number_1=float(input("enter the frsit number :"))
operator=input("enter an operator")
number_2=float(input("enter the second number :"))
if operator =='=':
    result=number_1+number_2
elif operator == '-':
    result=number_1-number_2
elif operator  == '*' :
    result=number_1*number_2
elif operator =='/':
    result=number_1/number_2
else :
    result=" invalid"
print(result)
