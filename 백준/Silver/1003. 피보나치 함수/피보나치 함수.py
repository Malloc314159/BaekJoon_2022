import sys
input=sys.stdin.readline

t=int(input())
zero=[1,0,1]
one=[0,1,1]
for i in range(3, 41):
    zero.append(zero[i-2]+zero[i-1])
    one.append(one[i-2]+one[i-1])
for i in range(t):
    n=int(input())
    print(zero[n], one[n])