#find BMI of a person where take mass and height as input from the user
#BMI=mass in kg / (height in m)2

mass=int(input("enter mass of the person in kg:"))
height=int(input("enter the height of the person in m:"))
bmi=mass/(height * height)
print("The BMI of the person is :",bmi,"kg/m\u00b2")