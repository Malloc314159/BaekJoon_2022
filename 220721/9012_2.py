n = int(input())
words = []
for i in range(n):
    words.append(input())

for i in words:
    while '()' in i:
        i = i.replace('()', '')
    if len(i)==0:
        print('YES')
    else:
        print('NO')