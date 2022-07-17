n=input()
for i in n:
    if i.islower():
        tmp=ord(i)+13
        if tmp>122:
            tmp=tmp-123+97
        i=chr(tmp)
    elif i.isupper():
        tmp=ord(i)+13
        if tmp>90:
            tmp=tmp-91+65
        i=chr(tmp)
    print(i, end='')