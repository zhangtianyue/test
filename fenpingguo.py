'''想通了就挺简单的，，如果苹果总数不能整除人数，证明无论怎么分，总会有人多出一些
苹果。 如果能整除，那么每个人的最终的苹果数目一定是平均数，不然不可能相等。所以
只需要把低于平均数那一部分补上，把高于平均数那一部分减掉就可以了。当然如果， 补
上的那一部分不能整除2，证明这个人是不能通过2个苹果的转移来达到平均数，即无论怎么
分，也不可能每个人的苹果都一样。'''
def fenpingguo():
    try:
        n=int(input())
        l_a=list(map(int,input().split()))#将苹果数转换为列表
        averapple=sum(l_a)/n#每个篮子的平均苹果数
        l_a.sort()
        m=0
        for i in l_a:
            if abs(i-averapple)%2!=0:
                return -1
            if i>=averapple:
                m+=(i-averapple)/2
        return int(m)
    except:
        pass
if __name__=='__main__':
    print(fenpingguo())