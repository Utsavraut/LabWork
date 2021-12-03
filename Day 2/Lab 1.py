# convert seconds to day, hours, minutes a
second = int(input("Enter the second:"))
day =  second/86400
hours= second/(24*60)
minute=second/24
print("Day =",day)
print("Hours =",hours)
print("Minute =",minute)