n=int(input())
dp=[0]*(n+1)
p=[0]*(n+1)
for i in range(2,n+1):
    dp[i]=dp[i-1]+1  # 1을 빼면서 시작
    p[i]=i-1
    if i%2==0:
        dp[i]=min(dp[i], dp[i//2]+1)
        if dp[i]==dp[i//2]+1:
            p[i]=i//2
    if i%3==0:
        dp[i]=min(dp[i], dp[i//3]+1)
        if dp[i]==dp[i//3]+1:
            p[i]=i//3

print(dp[n])
print(n, end=' ')
i=n
while p[i]!=0:
    print(p[i], end=' ')
    i=p[i]