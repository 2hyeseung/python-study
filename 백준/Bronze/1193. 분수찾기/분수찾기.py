# def findNum(n):
#     i=1
#     while True:
#         n-=i
#         if(n<=0):
#             return i+1
#             break
#         i+=1

# def sum(n):
#     res=0
#     for i in range(n):
#         res+=i+1
#     return res

# x=int(input())
# if(findNum(x)%2==0):
#     print(str(findNum(x)-(x-sum(findNum(x)-2)))+"/"+str(x-sum(findNum(x)-2)))
# else:
#     print(str(x-sum(findNum(x)-2))+"/"+str(findNum(x)-(x-sum(findNum(x)-2))))


x=int(input())
line=1

while(x>line):
    x-=line
    line+=1

if line%2==0:
    print(x,"/",line+1-x,sep='')
else:
    print(line+1-x,"/",x,sep='')
