n=int(input("Enetr the input of n: "))
def fib(n):
    a=0
    b=1
    if a<0:
        print("Invalid input")
    else:
        print(a)
        print(b)
    for i in range(2,n):
        if n==1:
            print(0)
        else:
            c=a+b
            a=b
            b=c
            print(c)

fib(n)