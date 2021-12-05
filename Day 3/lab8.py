#Given a n-digit number. Find the sum of its digits.
number = int(input("Enter a number"))
sumofDigits=0
for digit in str(number):
    sumofDigits += int(digit)
print(sumofDigits)
