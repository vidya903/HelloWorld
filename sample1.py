# Printing a Largest Number
num=input("Enter Numbers with spaces ")
numlist=num.split()
largest=str(0)
for i in numlist:
   if largest<i:
      largest=i
print (largest)



