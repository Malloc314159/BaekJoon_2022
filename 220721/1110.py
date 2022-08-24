n=int(input())
a=n//10
b=n%10
s=(a+b)%10
n1=b*10+s
i=1
while n1!=n:
    a=n1//10
    b=n1%10
    s=(a+b)%10
    n1=b*10+s
    i+=1
print(i)