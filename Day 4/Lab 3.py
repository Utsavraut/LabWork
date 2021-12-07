# #Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere11
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".

age=int(input("Enter your age:"))
gender=input("Enter your gender:")
if gender== "male" and age  in range(20,40):
    print("He can work anywhere")
elif gender=="female":
    print("She will work only in urban areas")
if gender== "male" and age  in range(40,60):
    print("He will work only in urban areas")
if age not in range (20,60):
    print("Error")