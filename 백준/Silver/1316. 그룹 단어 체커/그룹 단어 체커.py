import sys 
num=int(sys.stdin.readline())

inputs=[]
for i in range(num):
    inputs.append(sys.stdin.readline())

def isGroupWord(word):
    temp=""
    words=[]
    for i in range(len(word)):
        if(word[i] in words and temp!=word[i]):
            return False
        words.append(word[i])
        temp=word[i]
    return True

result=0
for i in inputs:
    if(isGroupWord(i)):
        result+=1
print(result)