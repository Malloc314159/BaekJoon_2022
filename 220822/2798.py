    import sys
    input=sys.stdin.readline
    n, m=map(int, input().strip().split())
    a=list(map(int, input().split()))
    ans=0
    for i in range(n):
        for j in range(i+1, n,1 ):
            for k in range(j+1, n, 1):
                if a[i]+a[j]+a[k]>m:
                    continue
                elif a[i]+a[j]+a[k]>ans:
                    ans=a[i]+a[j]+a[k]

    print(ans)