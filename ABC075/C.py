def dfs(p, reached):
    global N, G
    reached.append(p)
    for i in range(N):
        if G[p][i] and i not in reached:
            reached = dfs(i, reached[:])
    return reached

N, M = map(int, input().split())
G = [[False]*N for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1][b-1] = True
    G[b-1][a-1] = True

ans = 0
for i in range(N):
    for j in range(i):
        if G[i][j]:
            G[i][j] = False
            G[j][i] = False
            if len(dfs(0, [])) < N:
                ans += 1
            G[i][j] = True
            G[j][i] = True

print(ans)