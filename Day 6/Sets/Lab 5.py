#Write a Python program to remove an item from a set if it is present in the set.  
set = {"apple", "banana", "cherry"}
if "banana" in set:
     set.discard("banana")
print(set)