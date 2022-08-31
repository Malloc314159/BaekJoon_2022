import sys
input=sys.stdin.readline

a,b,c=map(int, input().strip().split())
def p(a,b,c):
    if b==1:
        return a%c
    elif b==2:
        return (a*a)%c
    else:
        if b%2==0:
            return ((p(a,b//2,c)**2))%c
        else:
            return ((p(a,b//2,c)**2)*a)%c
print(p(a,b,c))