num=int(input())
nums=[]

for i in range(num):
    nums.append(list(map(int,input().split())))

nums.sort(key=lambda x:x[1])
nums.sort(key=lambda x:x[0])

for i in range(len(nums)):
    print(nums[i][0],nums[i][1])