test=int(input())
testcase=[]
testres=[]

def avg(arr):
    sum=0
    for i in range(arr[0]):
        sum+=arr[i+1]
    return(sum/arr[0])

for i in range(test):
    testcase.append(list(map(int,input().split())))

for i in range(test):
    res=0
    # avg=avg(testcase[i])
    for j in range(testcase[i][0]):
        if(testcase[i][j+1]>avg(testcase[i])):
            res+=1
    testres.append(res/testcase[i][0]*100)

for i in range(test):
    print(f'{testres[i]:.3f}%')