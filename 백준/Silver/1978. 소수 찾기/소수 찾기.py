import sys
num=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
res=0

def isPrime(n):
    if(n==1):
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

for i in nums:
    if(isPrime(i)):
        res+=1

print(res)