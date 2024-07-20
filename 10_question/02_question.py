# Write a Python program that takes a student's score as input and determines their grade based on the
score=int(input("enter the students score"))
if score >=90 and score <= 100:
   print ("grade A")
elif score >= 80 and score <= 100 :
    print("gade B")
elif score >= 70 and score <= 100 :
   print ("grade C")
elif score >= 60 and score <= 100 :
   print ("grade D")
else :
    print("geade F")
