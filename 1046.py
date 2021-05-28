a,b=map(int,input().split())
if a>b and a>=12:
    x=24-a+b
    print(f"O JOGO DUROU {x} HORA(S)")
elif a<b and a<=12:
    z=b-a
    print(f"O JOGO DUROU {z} HORA(S)")
elif a==0 and b==0 or a==b:
    print(f"O JOGO DUROU 24 HORA(S)")