import sys
from collections import deque

input=int(sys.stdin.readline())
cards = [input-i for i in range(input)]
cards = deque(cards)

while(len(cards)>0):
    if(len(cards)==1):
        print(cards.pop())
        break
    cards.pop()
    cards.appendleft(cards.pop())