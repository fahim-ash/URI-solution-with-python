n=int(input())
list=[]
list.append(n)
j=0

if n<50:
    for i in range(0,10):
        n=n*2
        list.append(n)

for k in range(0, 10):
    p=list[k]
    print(f"N[{k}] = {p}")
