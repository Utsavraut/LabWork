#Write a program to find the factorial of a number using functions.
a=int(input("Enter a number: "))
j=1
def fac(a,j):
    for i in range (1, a+1):
        j=j*i
    print("Factoral: ",j)
fac(a,j)