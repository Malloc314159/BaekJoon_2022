n=int(input())
opened=0
yn=0
for i in range(n):
    a=input()
    opened=0
    yn=True
    for j in range(len(a)):
        if a[j]=='(':
            opened+=1
        elif a[j]==')':
            opened-=1
            if opened<0: yn=False
    if opened==0 and yn!=False:
        yn=True
    else:
        yn=False
    if yn:
        print('YES')
    else:
        print('NO')