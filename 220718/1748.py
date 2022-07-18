n=int(input())
N=len(str(n))
count=0
for i in range(N-1):
    count+=9*(10**i)*(i+1)
print(count+(n-(10**(N-1))+1)*N)