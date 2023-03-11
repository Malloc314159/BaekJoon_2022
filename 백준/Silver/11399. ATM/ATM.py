n=int(input())
a=list(map(int, input().split()))
a.sort()
sum=0
for i in range(n):
  for j in range(i+1):
    sum+=a[j]
print(sum)