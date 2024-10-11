import math

n = int(input())
a = list(map(int, input().split()))
cnt = [0]*n
for i in range(1, n):
    cnt[i] = math.ceil(math.log2(a[i-1]/a[i])) + cnt[i-1]
print(sum(cnt))