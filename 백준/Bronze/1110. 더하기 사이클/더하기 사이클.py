num=input()
newnum=num
res=0

while(True):
    if(len(newnum)<=1):
        newnum='0'+newnum
    sum=str(int(newnum[0])+int(newnum[1]))
    if(len(sum)<=1):
        sum='0'+sum
    newnum=newnum[-1]+sum[-1]
    res+=1
    if(int(num)==int(newnum)):
        break

print(res)