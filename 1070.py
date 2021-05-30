n=int(input())

if n%2==0:
    for i in range(n,n+13):
        if i%2!=0:
            print(i)
elif n%2!=0:
    for i in range(n,n+12):
        if i%2!=0:
            print(i)
