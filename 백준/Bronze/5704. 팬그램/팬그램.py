from string import ascii_lowercase

while True:
    a=input()
    alpha=list(ascii_lowercase)
    if a=='*': break
    for i in a:
        if i in alpha:
            alpha.remove(i)
    if len(alpha)==0:
        print('Y')
    else:
        print('N')