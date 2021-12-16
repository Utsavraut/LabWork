#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements 
lista=["apple","1","ball","56","good","12"]
for i in lista:
    if i!=lista[0] and i!=lista[4] and i!=lista[5]:
        print(i)
