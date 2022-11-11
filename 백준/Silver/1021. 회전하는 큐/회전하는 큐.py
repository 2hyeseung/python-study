import sys
from collections import deque

size, X = map(int, sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
res = 0

queue=[i+1 for i in range(size)]
queue=deque(queue)

for num in nums:
    while(True):
        if(queue[0]==num):
            queue.popleft()
            break
        elif(queue.index(num)>=len(queue)/2):   # 오른쪽 빼서 왼쪽에 추가
            res+=1
            queue.appendleft(queue.pop())
        else:                                   # 왼쪽빼서 오른쪽에 추가
            res+=1
            queue.append(queue.popleft())
print(res)