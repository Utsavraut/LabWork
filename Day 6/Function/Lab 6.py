#Write a Python program to reverse a string.
a=input("Enter a string: ")
j=len(a)-1
def rev(a,j):
    while j>=0:
        print(a[j],end="")
        j=j-1
rev(a,j)