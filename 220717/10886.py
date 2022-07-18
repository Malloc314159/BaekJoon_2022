n=int(input())
count=0
for i in range(n):
    t=int(input())
    if t==0: count+=1
if count>=(n+1)/2:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")