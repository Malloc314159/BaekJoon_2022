import sys
input=sys.stdin.readline

n, m=map(int, input().split())
a={}
for i in range(n):
  tmp=input().strip().split()
  a[tmp[0]]=tmp[1]
for i in range(m):
  tmp=input().strip()
  print(a[tmp])