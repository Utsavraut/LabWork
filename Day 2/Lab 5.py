# A school decided to replace the desks in three classrooms. Each desk sits two students.
# Given the number of students in each class, print the smallest possible number of desks
# that can be purchased.
# The program should read three integers: the number of students in each of the three
# classes, a, b and c respectively.
# Suppose In the first test there are three groups. The first group has 20 students and thus needs 10
# desks. The second group has 21 students, so they can get by with no fewer than 11 desks.
# 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.

A=int(input("Enter the number of students in first class:"))
B=int(input("Enter the number of students in second class:"))
C=int(input("Enter the number of students in third class:"))
if A%2==0:
    D=A/2
else:
    D=(A+1)/2 
if B%2==0:
    E=B/2
else:
    E=(B+1)/2
if C%2==0:
    F=C/2
else:
    F=(C+1)/2    
G=D+E+F
print("The number of desk in First class is:",D)
print("The number of desk in Second class is:",E)
print("The number of desk inThird class is:",F)
print("The total desk required is:",G)
    