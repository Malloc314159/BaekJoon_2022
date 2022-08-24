import sys
input=sys.stdin.readline

n=int(input())
li=[]
for i in range(n):
    x=input().strip()
    li.append([x, len(x)])
li.sort(key=lambda x: (x[1], x[0]))
out=[]
for i in range(n):
    if li[i][0] in out:
        continue
    print(li[i][0])
    out.append(li[i][0])