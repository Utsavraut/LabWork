#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
a=input("Enter a string: ")
upper=0
lower=0
others=0
def string(a, upper, lower, others):
    for i in a:
        if i.isupper()==True:
            upper=upper+1
        elif i.islower()==True:
            lower=lower+1
        else:
            others=others+1
    print("Uppercase letters: ",upper)
    print("Lowercase letters: ",lower)
    print("Other characters: ",others)
string(a,upper,lower,others)