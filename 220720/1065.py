count=0
for i in range(1, int(input())+1):
    j=str(i)
    j=list(map(int, j))
    if len(j)==1 or len(j)==2:
        count+=1
    elif len(j)==3:
        if j[0]-j[1]==j[1]-j[2]:
            count+=1
print(count)