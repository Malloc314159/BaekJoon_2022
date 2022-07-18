n=1000-int(input())
count=0
arr=[500,100,50,10,5,1]
tmp=0
while True:
    if n==0: break
    if arr[tmp]<=n:
        n-=arr[tmp]
        count+=1
    else:
        tmp+=1
print(count)