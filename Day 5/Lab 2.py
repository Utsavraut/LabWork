#Write a Python program to convert temperatures to and from celsius, fahrenheit.
C=int(input("Enter the temprature in celcius:"))
F=int(input("Enter the temprature in fahrenheit:"))
faren=(C*1.8)+32
print("The temp coverted in farenheit is:",faren)
celcius=(F-32)/1.8
print("The temp coverted in Celcius is:",celcius)
