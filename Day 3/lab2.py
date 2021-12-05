#WAP which accepts marks of four subjects and display total marks, percentage and grade. 
# Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 

Math=int(input("Enter the marks in  maths:"))
Science=int(input("Enter the marks in  science:"))
English=int(input("Enter the marks in  english:"))
Nepali=int(input("Enter the marks in  nepali:"))
Total=Math+Science+English+Nepali
print("The total marks is:",Total)
Percentage=(Total/400)*100
print("The percantage is:",Percentage,"%")
if Percentage>70:
    print("You got  Distinction")
elif Percentage>60 and Percentage<70:
    print("You got first Division")
elif Percentage>40 and Percentage<60:
    print("You are passs")
else:
    print("You are fail")
    