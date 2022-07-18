import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1, 1):
        if n%i==0:
            return False
    return True

n=int(input().strip())
num=input().strip().split()
num=list(map(int, num))
count=0
for i in range(n):
    if num[i]==1:
        continue
    elif isPrime(num[i]):
        count+=1
print(count)