# 将列表转换为集合来删除重复项目，再用len函数计算集合长度。
import sys
a=[]
for line in sys.stdin:
    if line.strip() == '':
        break
    a.extend(line.split())
print(len(set(a)))