# Printing a Armstrong Number
num = input("Enter a Number ")
length = 1
length = length + len(num)
arm_stg = 0
for char in (num):
    arm_stg = arm_stg + (int(char) ** (length - 1))
    num = int(num)
    arm_stg = int(arm_stg)
if (arm_stg - num == 0):
    print("It is a Armstrong number")
else:
    print("It is not a Armstrong number")


