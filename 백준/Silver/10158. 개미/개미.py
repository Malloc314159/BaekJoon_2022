w,h=map(int, input().split())
x,y=map(int, input().split())
t=int(input())
dir=0
for i in range(t%(2*w)):
  if dir==0:
    x+=1
  else:
    x-=1
  if x==w:
    dir=-1
  if x==0:
    dir=0
dir=0
for i in range(t%(2*h)):
  if dir==0:
    y+=1
  else:
    y-=1
  if y==h:
    dir=-1
  if y==0:
    dir=0
print(x,y)