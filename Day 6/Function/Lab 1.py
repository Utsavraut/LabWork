#Write a Python function to find the Max of three numbers 
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter another number: "))
def greatest(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    elif c>a and c>b:
        print(c)
    else:
        print("Two numbers might be equal")
greatest(a,b,c)