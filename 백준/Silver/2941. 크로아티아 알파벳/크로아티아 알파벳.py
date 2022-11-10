import sys

c_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
input=sys.stdin.readline().strip()

for alphabet in c_alphabet:
    input=input.replace(alphabet,'#')
print(len(input))
