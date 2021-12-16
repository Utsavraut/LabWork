#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2 
lista=["eye","dead","1221","abc","aaa"]
y=0
for i in lista:
    if len(i)>2:
        if i[0]==i[len(i)-1]:
            y=y+1
print(y)