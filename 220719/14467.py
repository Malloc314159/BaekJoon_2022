n=int(input())
cow=[-1]*10
count=0
for _ in range(n):
    t=input().split()
    t=list(map(int, t))
    if cow[t[0]-1]==-1:
        cow[t[0]-1]=t[1]
    elif cow[t[0]-1]!=t[1]:
        count+=1
        cow[t[0]-1]=t[1]
print(count)