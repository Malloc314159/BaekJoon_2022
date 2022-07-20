for i in range(int(input())):
    a=input().split()
    arr=[]
    for j in range(len(a[1])):
        arr+=[a[1][j]]*int(a[0])
    print(''.join(arr))