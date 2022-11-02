len=int(input())
nums=list(map(int,input().split()))
max_num=max(nums)
sum=0

for i in range(len):
    sum+=nums[i]

print(sum*100/max_num/len)