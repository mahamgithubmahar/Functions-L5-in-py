def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
num=int(input("Enter a number "))
if num<0:
    print("sorry, numbers below 0 are not allowed")
elif num==1:
    print("factorial is 1")
else:
    print(factorial(num))