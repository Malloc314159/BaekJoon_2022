import math
m=int(input())
n=int(input())
prime=[]
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for i in range(m, n+1):
    if i!=1 and isPrime(i):
        prime.append(i)
if len(prime)==0: print(-1)
else:
    print(sum(prime))
    print(min(prime))