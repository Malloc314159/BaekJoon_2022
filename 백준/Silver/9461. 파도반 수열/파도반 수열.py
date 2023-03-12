import sys
input=sys.stdin.readline

t=int(input())
dp=[1]*100
dp[3]=2
dp[4]=2
dp[5]=3
for i in range(6,100):
  dp[i]=dp[i-1]+dp[i-5]
for i in range(t):
  n=int(input())
  print(dp[n-1])  