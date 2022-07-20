n=int(input())
b=input().split()
b=list(map(int, b))
a=[b[0]]
for i in range(1,n):
    a.append(b[i]*(i+1)-sum(a[:i]))
a=list(map(str, a))
print(' '.join(a))