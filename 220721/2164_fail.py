n=int(input())
card=[]
for i in range(n):
    card.append(i+1)
while len(card)>1:
    card.pop(0)
    card.append(card[0])
    card.pop(0)
print(card[0])