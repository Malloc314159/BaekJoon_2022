n=int(input())
max=[' ',32,13,3000]
min=[' ',0,0,1980]
def ch1():
    for k in range(4):
        max[k] = a[k]

def ch2():
    for k in range(4):
        min[k] = a[k]

for i in range(n):
    a=input().split()
    j=3
    for j in range(1,4):
        a[j]=int(a[j])
    if a[3]<max[3]:
        ch1()
    elif a[3]==max[3]:
        if a[2]<max[2]:
            ch1()
        elif a[2]==max[2]:
            if a[1]<max[1]:
                ch1()
    if a[3] > min[3]:
        ch2()
    elif a[3] == min[3]:
        if a[2] > min[2]:
            ch2()
        elif a[2] == min[2]:
            if a[1] > min[1]:
                ch2()

print(min[0])
print(max[0])