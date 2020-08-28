print("Fibonacci numbers using command line ")
import sys
def fib(n):
    a,b=0,1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(n):
        fib=a+b
        a,b=b,fib
        print(fib(sys.argv[1]),end=" ")
