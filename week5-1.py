n=int(input("Enter a number:"))
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print("Fibonacci series with recursion:")
for i in range(1,n+1):
    print(fib(i),end=" ")
print("\nFibonacci without recursion")
fib1=0
fib2=1
for j in range(1,n+1):
    print(fib1,end=" ")
    temp=fib1
    fib1=fib2
    fib2=temp+fib2
