import sys
from collections import deque

input=int(sys.stdin.readline())
cards = [input-i for i in range(input)]
cards = deque(cards)

while(len(cards)>0):
    print(cards.pop())
    if(len(cards)==0):
        break
    else:
        cards.appendleft(cards.pop())