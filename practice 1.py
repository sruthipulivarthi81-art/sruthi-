n=int(input("enter the number"))
if n>1:
    fact=0
    for i in range(1,n+1):
        if (n%i==0):
            fact=fact+1
    if fact==2:
                print("pime number")
    else:
                print("not a prime number")
