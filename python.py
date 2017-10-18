#设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
from functools import cmp_to_key
def cmp(a,b):
    ab = int(a + b)
    ba = int(b + a)
    if ab > ba:
        return 1
    else:
        return -1
n = int(input())
list=input().split(' ')
list.sort(key=cmp_to_key(cmp),reverse=True)
print(int(''.join(list)))