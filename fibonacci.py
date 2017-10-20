'''不必进行查找，也不必存储斐波那契数列，可直接快速获取返回值
循环生成斐波那契数，当生成第一个比n大的斐波那契数时， 此时离n最近的两个斐波那契数为最新生成的两个斐波那契数，
测试它们，返回与n之间的最小距离。'''
def fibonacci():
    N=int(input())
    a=0
    b=1
    while True:
        if b>N:
            return min(N-a,b-N)
        a,b=b,a+b#如果写到两行会产生逻辑错误
print(fibonacci())