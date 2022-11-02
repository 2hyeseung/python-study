nums=[]
while(True):
    num=input()
    if(num=="0"):
        break
    else:
        nums.append(num)

def isPalindrome(n):
    for i in range(len(n)//2):
        if(n[i]!=n[len(n)-i-1]):
            return False
    return True

for i in nums:
    if(isPalindrome(i)):
        print("yes")
    else:
        print("no")
