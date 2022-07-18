import copy
s=input()
a=[]
for i in range(len(s)):
    tmp=list(copy.deepcopy(s))
    for j in range(i):
        del tmp[0]
    a.append(tmp)
a=list(sorted(a))
for i in range(len(a)):
    print(''.join(a[i]))