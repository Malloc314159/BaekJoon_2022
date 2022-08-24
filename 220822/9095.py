t=int(input())
a=[1,2,4]
for _ in range(t):
    n=int(input())
    for i in range(len(a),n,1):
        a.append(a[i-1]+a[i-2]+a[i-3])
    print(a[n-1])