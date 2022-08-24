t=int(input())
a=[1,2,4]
for _ in range(t):
    n=int(input())
    for i in range(len(a),n,1):
        a.append(a[i-1]%1000000009+a[i-2]%1000000009+a[i-3]%1000000009)
    print(a[n-1]%1000000009)