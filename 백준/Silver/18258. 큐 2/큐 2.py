from collections import deque
import sys

input_num=int(sys.stdin.readline())
inputs=[]
queue=deque()

for i in range(input_num):
    inputs.append(sys.stdin.readline().strip())

for input in inputs:
    if 'push' in input:
        push, x = input.split(" ")
        queue.append(x)
        continue
    if input=='size':
        print(len(queue))
        continue
    if(len(queue)==0):
        if(input=='front' or input =='back' or input=='pop'):
            print("-1")
        else:
            print("1")
    else:
        if(input=='front'):
            temp=queue.popleft()
            print(temp)
            queue.appendleft(temp)
        elif(input=='back'):
            temp=queue.pop()
            print(temp)
            queue.append(temp)
        elif(input=='pop'):
            print(queue.popleft())
        else:
            print("0")