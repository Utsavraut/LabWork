#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

class_held=int(input("enter the number of classes held:"))
class_attended=int(input("enter the number of classes attended:"))
print("The number of class held is:",class_held)
print("The number of class attended is:",class_attended)
percantage=(class_attended/class_held)*100
print("The total percaentage is :",percantage,"%")
if percantage < 75:
    print("student is not allowed to sit in exam")
else:
    print("student is allowed to sit in exam")