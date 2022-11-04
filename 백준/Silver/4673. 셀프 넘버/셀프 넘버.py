all_num=set(range (1,10001))
not_self_num=set()

# 전체 숫자에서 셀프넘버가 아닌 숫자를 뺀다
for i in range(10000):
    length=len(str(i))
    num=i
    for j in range(length):
        num+=int(str(i)[j])
    not_self_num.add(num)

# 차집합
for i in sorted(all_num.difference(not_self_num)):
    print(i)