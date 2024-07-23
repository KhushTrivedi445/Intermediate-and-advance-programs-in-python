#Fibonacci using recusion

def fibo(n):
    if n==0 or n==1 :
        return n   
    else:
        return fibo(n-1)+fibo(n-2)

x=int(input("Enter till how much terms you want the series : "))
print("The fibonacci serires is :" )
for i in range (x+1) :
    print(fibo(i))
    