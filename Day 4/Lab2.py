#Write a Python program to sum three given integers. However, if two or more values are equal sum will be zero.
Num_1=int(input("Enter First number:"))
Num_2=int(input("Enter Second number:"))
Num_3=int(input("Enter Third number:"))
sum =0
if Num_1==Num_2==Num_3:
    print(sum)
else:
    Total=Num_1+Num_2+Num_3
    print("The sum is:",Total)
    
