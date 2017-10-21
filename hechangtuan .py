def main():
    n,m = list(map(int,input().split()))
    b=[]
    for i in range(n):
        b.append(input())
    x0,y0 = list(map(int,input().split()))#起始位置
    k = int(input())
    alternatives = []
    for i in range(k):
        alternatives.append(list(map(int,input().split())))
    step = [[-1]*m for i in range(n)]
    arrive = [[0]*m for i in range(n)]
    if b[x0][y0] != '.':
        return -1
    arrive[x0][y0] = 1
    step[x0][y0] = 0
    curr = [[x0,y0]]
    while len(curr):
        nextpos = []
        for p in curr:
            x,y = p[0],p[1]
            for s in alternatives:
                x_,y_ = x+s[0],y+s[1]
                if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m:
                    continue
                if  b[x_][y_] != '.' or arrive[x_][y_] == 1:
                        continue
                else:
                    step[x_][y_] = step[x][y]+1
                    arrive[x_][y_] = 1
                    nextpos.append([x_,y_])
        curr = nextpos
    ms = 0
    for i in range(n):
        for j in range(m):
            if step[i][j] == -1 and b[i][j]=='.':
                return -1
            ms = max(ms,step[i][j])
    return ms
print(main())