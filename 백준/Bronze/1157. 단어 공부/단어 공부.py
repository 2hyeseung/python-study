from string import ascii_uppercase
alphabet_dict={}

for i in ascii_uppercase:
    alphabet_dict[i]=0

str=input().upper()

for i in range(len(str)):
    alphabet_dict[str[i]]+=1

answer=[]
for key,value in alphabet_dict.items():
    if value==max(alphabet_dict.values()):
        answer.append(key)
if(len(answer)>1):
    print("?")
else:
    print(answer[0])