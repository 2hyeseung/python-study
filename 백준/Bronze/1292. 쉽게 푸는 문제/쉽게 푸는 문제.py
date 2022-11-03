a,b = map(int,input().split())

arr=[]
for i in range(46):     # 범위가 1000까지기 때문
    for j in range(i):
        arr.append(i)
 
print(sum(arr[a-1:b]))