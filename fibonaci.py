def fibo(n):
    a=0
    b=1
    if n==1:
       print(a)
    elif n==2:
        print(str(a)+" , "+str(b),end="")
    else:
            if n<=0:
                print("Incorrect number\n")
            else:
                print(str(a)+" , "+str(b),end="")
    for i in range(2,n):
        sum=a+b
        a=b
        b=sum
        print(" , "+str(sum),end="")

n=int(input("Enter number to find series:"))
fibo(n)
