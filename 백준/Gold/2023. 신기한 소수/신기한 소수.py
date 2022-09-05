import sys
import math
input=sys.stdin.readline

def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def dfs(num):
    if len(str(num))==n: # 자릿수가 n이라면 출력
        print(num)
    else:
        for i in range(10):
            t=10*num+i
            if isPrime(t):
                dfs(t)
n=int(input())
# 어차피 소수인 한자릿수는 2,3,5,7밖에 없음
dfs(2)
dfs(3)
dfs(5)
dfs(7)