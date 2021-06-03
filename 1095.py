list=[]
list2=[]

for i in range(1,40,3):
    list.append(i)
for j in range(60,-5,-5):
    list2.append(j)
for k in range(0,13):
    a=list[k]
    b=list2[k]

    print(f"I={a} J={b}")
