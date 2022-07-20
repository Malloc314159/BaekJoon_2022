n=input().split()
n=list(map(int, n))
l1=[1,2,3,4,5,6,7,8]
l2=[8,7,6,5,4,3,2,1]
if (n==l1): print('ascending')
elif (n==l2): print('descending')
else: print('mixed')