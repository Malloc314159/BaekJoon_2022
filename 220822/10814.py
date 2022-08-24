import sys
input=sys.stdin.readline
n=int(input())
li=[]
for i in range(n):
    a,b=input().split()
    a=int(a)
    li.append([i, a, b])
li.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(li[i][1], li[i][2])