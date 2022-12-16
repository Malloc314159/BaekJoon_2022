import heapq

t=int(input())
for _ in range(t):
    hq = []
    hq2 = []
    k=int(input())
    isThere = [False] * k

    for i in range(k):
        a=input().split()
        if a[0]=='I':
            heapq.heappush(hq, (int(a[1]), i))  # 최소 pop
            heapq.heappush(hq2, (-int(a[1]), i))    # 최대 pop
            isThere[i]=True
        else:
            if a[1]=='1':
                while hq2 and not isThere[hq2[0][1]]: # hq2의 원소가 모두 없어지거나 / id배열의 (hq2 중 가장 앞에 있는 원소의 id)번째의 인덱스가 True 값일 때까지 반복
                    heapq.heappop(hq2)
                if hq2: # hq2의 원소가 남아있을 경우 (=배열의 (hq2 중 가장 앞에 있는 원소 id)번째 인덱스가 True-> 실제로 값이 있다!)
                    isThere[hq2[0][1]]=False
                    heapq.heappop(hq2)
            else:
                while hq and not isThere[hq[0][1]]:
                    heapq.heappop(hq)
                if hq:
                    isThere[hq[0][1]]=False
                    heapq.heappop(hq)

    while hq and not isThere[hq[0][1]]:
        heapq.heappop(hq)
    while hq2 and not isThere[hq2[0][1]]:
        heapq.heappop(hq2)

    if hq and hq2:
        print(-hq2[0][0], hq[0][0])
    else:
        print('EMPTY')