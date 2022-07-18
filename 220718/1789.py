import sys
n=int(input())
if n==1:
    print(1)
    sys.exit()
for i in range(1,n+1):
    sum=(i*(i+1))/2
    if sum>n:
        print(i-1)
        break