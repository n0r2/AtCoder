from collections import deque


def dfs(p):
    global L
    ret = []
    for i in L[p]:
        for j in L[i]:
            for k in L[j]:
                if k not in ret:
                    ret.append(k)
    return ret


N, M = map(int, input().split())
L = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    L[A - 1].append(B - 1)
    L[B - 1].append(A - 1)

print(dfs(0))

ans = 0
flug = True
while flug:
    flug = False
    for i in range(N):
        three = dfs(i)
        print(three)
        for j in three:
            if j not in L[i]:
                L[i].append(j)
                L[j].append(i)
                ans += 1
                flug = True
                break

print(L)
print(ans)
