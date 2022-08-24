import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
dq=deque()
for _ in range(n):
    a=list(input().split())
    if a[0]=='push':
        dq.append(a[1])
    elif a[0]=='pop':
        if len(dq)==0:
            print(-1)
        else:
            print(dq.popleft())
    elif a[0]=='size':
        print(len(dq))
    elif a[0]=='empty':
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif a[0]=='front':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0])
    elif a[0]=='back':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[len(dq)-1])