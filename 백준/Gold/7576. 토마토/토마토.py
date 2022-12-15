import sys
from collections import deque
input=sys.stdin.readline

m,n=map(int, input().strip().split())
tomato=[list(map(int, input().strip().split())) for _ in range(n)]
queue=deque([])
x_dir, y_dir=[-1,1,0,0], [0,0,-1,1] # 이차원 배열에서 상하좌우(순서대로) 표현
day=0
for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            queue.append([i, j])

def bfs():
    global day
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx, ny = x_dir[i]+x, y_dir[i]+y
            if 0<=nx<n and 0<=ny<m:
                if tomato[nx][ny]==0:
                    tomato[nx][ny]=tomato[x][y]+1
                    queue.append([nx, ny])

bfs()
for i in tomato:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    day=max(day, max(i))
print(day-1)