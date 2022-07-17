import string

stringArr=input()
alpha=string.ascii_lowercase
count=[]
for i in range(26):
    count.append(-1)
for i in range(len(stringArr)):
    tmp=alpha.find(stringArr[i])
    if count[tmp]==-1:
        count[tmp]=i

for i in range(26):
    print(str(count[i]), end=' ')