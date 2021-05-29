n=int(input())
for i in range(0,n):
    a,b,c,d=map(str,input().split())
    x,y=map(int,input().split())
    if (x+y)%2==0:
        if b=="PAR":
            print(a)
        else:
            print(c)
    elif (x+y)%2==1:
        if b=="IMPAR":
            print(a)
        else:
            print(c)
