num=int(input())
array=[]

for i in range(num):
    array.append(input())
answer=list(array[0])

for i in range(num):
    for j in range(len(array[0])):
        if(answer[j]!=array[i][j]):
            answer[j]="?"

for i in answer:
    print(i,end='')