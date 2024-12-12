n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
 fact=fact*i
print(n,"! =",fact)

n=int(input("Enter the number: "))
fib=0
print("Fibonacci SERIES:")
for i in range(0,n+1):
 fib=fib+i
print(fib)

a=[45,34,70,48,37,50]
print("Sum is: ",sum(a))