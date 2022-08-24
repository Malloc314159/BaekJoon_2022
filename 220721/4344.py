n=int(input())
for i in range(n):
    a=list(map(int, input().split()))
    a.pop(0)
    p=sum(a)/len(a)
    s=0
    for j in a:
        if j>p: s+=1
    result=100*s/len(a)
    print(f'{result:.3f}'+'%')