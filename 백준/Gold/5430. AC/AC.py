import sys
from collections import deque
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    f=input().strip()
    n=int(input().strip())
    a=input().strip('[').strip(']\n')
    if len(a)==0:
        if 'D' in f:
            print('error')
            continue
        else:
            print('[]')
            continue
    a=deque(map(int, a.split(',')))
    error=False
    reverse=False
    for i in f:
        if i=='R':
            reverse=not reverse
        else:
            if len(a)!=0:
                if reverse:
                    a.pop()
                else:
                    a.popleft()
            else:
                error=True
                break
    if error:
        print('error')
    else:
        if reverse:
            a.reverse()
        print(str(a)[6:-1].replace(' ', ''))