n=int(input())
while n//10>0:
    n=list(map(int, str(n)))
    n=sum(n)
print(n)
print('YES' if n%3==0 else 'NO')