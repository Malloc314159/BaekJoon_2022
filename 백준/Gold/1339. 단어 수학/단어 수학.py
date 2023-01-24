n=int(input())
a=dict()
for i in range(n):
    tmp=input()
    for j in range(len(tmp)):
        if tmp[j] in a:
            a[tmp[j]]+=10**(len(tmp)-j-1)
        else:
            a[tmp[j]]=10**(len(tmp)-j-1)
a=sorted(a.items(), key=lambda item:item[1], reverse=True)    # Value를 기준으로 정렬
p=9
sum=0
for i in a:
    sum+=p*i[1]
    p-=1
print(sum)