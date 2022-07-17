a=input().split(' ')
b=input().split(' ')
c=input().split(' ')
d=[0,0]
for i in range(2):
    if a[i]==b[i]:
        d[i]=c[i]
    elif b[i]==c[i]:
        d[i]=a[i]
    else:
        d[i]=b[i]
    print(d[i], end=' ')