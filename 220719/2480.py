n=input().split()
n=list(map(int, n))
if n[0]==n[1] and n[1]==n[2]:
    print(10000+1000*n[0])
elif n[0]==n[1] or n[1]==n[2]:
    print(1000+100*n[1])
elif n[0]==n[2]:
    print(1000+100*n[0])
else:
    print(100*max(n))