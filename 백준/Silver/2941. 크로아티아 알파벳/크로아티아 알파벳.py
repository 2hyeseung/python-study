import sys

c_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
input=sys.stdin.readline().strip()

# str1.count(str2) : 문자열 안에 문자열 몇개 있는지 확인
for alphabet in c_alphabet:
    input=input.replace(alphabet,'#')
print(len(input))