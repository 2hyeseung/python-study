import sys
from collections import deque

length, num = map(int, sys.stdin.readline().split())
queue=deque()
result=[] 

for i in range(length):
    queue.append(i+1)

while queue:
    for i in range(num-1):
        queue.append(queue.popleft())   # 삭제할 숫자 앞에꺼들을 삭제하고 뒤로 붙임
    result.append(queue.popleft())      # 삭제할 숫자 삭제

# 정답리스트result => map함수:str변환 => join:,추가
# join은 str에만 쓸수있기 때문
print("<"+", ".join(list(map(str,result)))+">")