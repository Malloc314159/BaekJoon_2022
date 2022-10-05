import sys
import heapq as hq

input=sys.stdin.readline
n=int(input().strip())
a=[]

for _ in range(n):
    t=int(input().strip())
    if t==0:
        if len(a) == 0:
            print(0)
        else:
            print(hq.heappop(a)*-1)
    else:
        hq.heappush(a,-1*t)