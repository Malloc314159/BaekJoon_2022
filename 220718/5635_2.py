n=int(input())
data=[]
name=[]
for i in range(n):
    a=input().split()
    name.append(a[0])
    data.append(int(a[1])+int(a[2])*30+int(a[3])*365)
print(name[data.index(max(data))])
print(name[data.index(min(data))])