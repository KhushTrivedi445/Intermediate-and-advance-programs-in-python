# Factorial using recursion

def factorial(n):
    if n==1:
        return 1
    else :
        return n*factorial(n-1)
    
x=int(input("Enter the number that you want to find the factorial :"))
print("The factorial is : ",factorial(x))
