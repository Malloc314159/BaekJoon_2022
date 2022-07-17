import string
stringArr=input()
alpha=string.ascii_lowercase
count=[]
for i in range(26):
    count.append(0)
for i in stringArr:
    tmp=alpha.find(i)
    count[tmp]+=1
for i in range(26):
    print(str(count[i]), end=' ')