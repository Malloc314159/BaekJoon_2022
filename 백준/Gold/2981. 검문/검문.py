import sys
import math
input=sys.stdin.readline

def gcd(a,b):
    while b:
        t=b
        b=a%b
        a=t
    return a


n=int(input().strip())
li=sorted([int(input().strip()) for _ in range(n)])
li2=[]
for i in range(n-1):
    li2.append(li[i+1]-li[i])
g=li2[0]
for i in range(1,n-1):
    g=gcd(g,li2[i])
a=[g]
for i in range(2,int(math.sqrt(g))+1):
    if g%i==0:
        a.append(i)
        if g//i != i:
            a.append(g//i)
a=sorted(a)
for i in a:
    print(i, end=' ')