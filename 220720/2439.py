n=int(input())
for i in range(n):
    tmp=['*']*(i+1)
    print(''.join(tmp).rjust(n))