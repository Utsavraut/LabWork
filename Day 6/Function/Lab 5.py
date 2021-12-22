# Write a function called show_stars(rows). If rowsis 5, it should print the following:•* •** •*** •**** •***** 
a=int(input("Enter a number of rows: "))
def star(a):
    for i in range(a+1):
        for j in range(i):
            print("*",end=" ")
        print()
star(a)