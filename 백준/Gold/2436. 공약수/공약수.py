import sys
input=sys.stdin.readline

def gcd(a,b):  # gcd function with euclidean algorithm
    while b:
        t=b
        b=a%b
        a=t
    return a

g,l=map(int, input().strip().split())
dv=l//g
a,b=1, dv
for i in range(1,dv//2+1):
    if dv%i==0:
        c=i
        d=dv//i
    if gcd(c,d)!=1:
        continue
    if a+b>c+d:
        a=c
        b=d
print(a*g,b*g)