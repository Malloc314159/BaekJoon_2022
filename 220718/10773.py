k=int(input())
sum=0
li=[]
for _ in range(k):
    t=int(input())
    if t==0: del li[len(li)-1]
    else: li.append(t)
for i in range(len(li)):
    sum+=li[i]
print(sum)