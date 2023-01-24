n=int(input())
count=0
if n%5==0:
    print(n//5)
else:
    while n>0:
        n-=3
        count+=1
        if n%5==0:
            print(n//5+count)
            break
        elif n==0:
            print(count)
        elif n==1 or n==2:
            print(-1)