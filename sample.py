# Printing a LCM of a two numbers
num1=int(input("Enter Numbers one: "))
num2=int(input("Enter Numbers two: "))
value=1
for i in range(2,num1):
  if num1%i==0:
     if i==2 or i==3:
        value=(value*i)
     else i//2==2:
         value=(value)*i/2
     else i//3==:
         value=(value)*i/3
     elif:
         value=value*i
      print (value)


