import sys
import math
input=sys.stdin.readline

n=int(input().strip())
pr=[True for _ in range(n+1)]

# 에라토스테네스의 체
for i in range(2,int(math.sqrt(n))+1):
    if pr[i]:
        for j in range(i*2,n+1,i):
            pr[j]=False

p_num=[]
for i in range(2,n+1):
    if pr[i]:
        p_num.append(i)

c=0
sum=0
end=0

for start in range(len(p_num)):
    while sum<n and end<len(p_num):
        sum+=p_num[end]
        end+=1
    if sum==n:
        c+=1
    sum-=p_num[start]

print(c)