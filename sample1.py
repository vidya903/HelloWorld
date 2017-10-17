# Factorial of a number
def factorial(n):
  rev=1
  for i in range(1,n+1):
    rev=rev*i
  return rev


while True:
  n=int(input("Enter a Number "))
  if (n==0):
    break
  else:
    res = factorial(n)
    print (res)
