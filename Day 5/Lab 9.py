#Write a program to find the factorial of a number.
a=int(input("Enter a number: "))
j=1
for i in range (1, a+1):
    j=j*i
print("Factoral: ",j)