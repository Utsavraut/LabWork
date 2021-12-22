#Accept string from the user and display only those characters which are present at an even index 
a=input("Enter a string: ")
def even_string(a):
    for i in range(1,len(a),2):
        print(a[i])
even_string(a)