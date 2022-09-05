import sys
import heapq
input=sys.stdin.readline

n=int(input().strip())
a=[]
c=0
for i in range(n):
    heapq.heappush(a, int(input().strip()))

if n==1:
    print(0)
else:
    while len(a)>1:
        s=heapq.heappop(a)+heapq.heappop(a)
        c+=s
        heapq.heappush(a,s)
    print(c)