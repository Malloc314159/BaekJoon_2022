arr1=[]
arr3=[]
for i in range(10000):
  arr1.append(i)
for i in range(10000):
  arr2=list(map(int,str(i)))
  arr3.append(sum(arr2)+i)
result=list(set(arr1)-set(arr3))
result.sort()
for i in result:
  print(i)