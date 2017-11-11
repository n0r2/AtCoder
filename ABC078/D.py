def fx(p, x, y):
    global a, X
    if p == len(a):
        return abs(x - y)
    if x in X[p] and y in X[p][x]:
        return X[p][x][y]
    ret = 0
    for i in range(p, len(a)):
        ret = max(fy(i+1, a[i], y), ret)
    if x not in X[p]:
        X[p][x] = {y: ret}
    else:
        X[p][x][y] = ret
    print('fx', p, x, y, ret)
    return ret


def fy(p, x, y):
    global a, Y
    if p == len(a):
        return abs(x - y)
    if x in Y[p] and y in Y[p][x]:
        return Y[p][x][y]
    ret = float('inf')
    for i in range(p, len(a)):
        ret = min(fy(i+1, x, a[i]), ret)
    if x not in Y[p]:
        Y[p][x] = {y: ret}
    else:
        Y[p][x][y] = ret
    print('fy', p, x, y, ret)
    return ret


N, Z, W = map(int, input().split())
a = list(map(int, input().split()))
X = [{} for i in range(len(a))]
Y = [{} for i in range(len(a))]

print(fx(0, Z, W))
