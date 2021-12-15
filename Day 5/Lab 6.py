#Write a Python program to count the number of even andodd numbers from a series of numbers.
a=int(input("Enter a number: "))
j=0
k=0
for i in range(1,a+1):
    if i%2==0:
        j+=1
    else:
        k+=1
print("Number of even numbers: {}".format(j))
print("Number of odd numbers: {}".format(k))