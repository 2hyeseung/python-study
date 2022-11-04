# sys : 처리속도가 더 빠르다
# sys.stdin.readline()
import sys 

num=int(sys.stdin.readline())
nums=[]

for i in range(num):
    nums.append(int(sys.stdin.readline()))

for i in sorted(nums):
    print(i)