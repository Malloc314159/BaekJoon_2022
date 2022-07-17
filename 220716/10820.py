while True:
    try:
      n=input()
      count=[0]*4
      for i in n:
        if i>='A' and i<='Z':
            count[1]+=1
        elif i>='a' and i<='z':
            count[0]+=1
        elif i>='0' and i<='9':
            count[2]+=1
        elif i==' ':
            count[3]+=1
        else:
            break
      print(*count)
    except EOFError:
        break