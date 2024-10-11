n = int(input())
a = list(map(int, input().split()))
t = [2**i for i in range(21)]
cnt = 0
k = 0
for i in range(1, n):
    k = 0
    while t[k] < (a[i - 1] / a[i]):
        k += 1
        cnt += 1
    a[i] *= t[k]
print(cnt)
