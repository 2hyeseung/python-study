num=int(input())
list=[]

def res(str):
    res=0
    stack=0
    for i in range(len(str)):
        if(str[i]=="O"):
            res+=stack+1
            stack+=1
        else:
            stack=0
    return res
    

for i in range(num):
    list.append(input())

for i in range(num):
    print(res(list[i]))
