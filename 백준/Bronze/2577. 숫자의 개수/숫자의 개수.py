num1=int(input())
num2=int(input())
num3=int(input())
num=str(num1*num2*num3)
res=[0,0,0,0,0,0,0,0,0,0]

for i in range(0,len(num)):
    res[int(num[i])]+=1

for i in res:
    print(i)
    