import sys
input=sys.stdin.readline

dp=[0]*1000
dp[0]=1
dp[1]=3
n=int(input())
for i in range(2,n):
  dp[i]=(2*dp[i-2]+dp[i-1])%10007
print(dp[n-1])