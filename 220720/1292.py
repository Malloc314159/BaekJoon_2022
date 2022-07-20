n, m=input().split()
arr=[]
for i in range(1, 100):
    for j in range(i):
        arr.append(i)
    if len(arr)>int(m): break
print(sum(arr[int(n)-1:int(m)]))