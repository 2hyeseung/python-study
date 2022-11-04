import sys 
num=int(sys.stdin.readline())

inputs=[]
for i in range(num):
    inputs.append(list(map(int,sys.stdin.readline().split())))

def func(p):
    res=0
    for i in range(num):
        if(i!=p):
            if(inputs[p][0]>=inputs[i][0] or inputs[p][1]>=inputs[i][1]):
                res+=1
    return num-res

for i in range(num):
    print(func(i),end=" ")