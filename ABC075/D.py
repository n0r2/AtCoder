import itertools

N, K = map(int, input().split())

point = [tuple(map(int, input().split())) for i in range(N)]

ans = float('inf')

for i, j, k, l in itertools.product(point, repeat=4):
    x1, x2, y1, y2 = i[0], j[0], k[1], l[1]
    if x2 <= x1 or y2 <= y1:
        continue
    count = 0
    for p in point:
        if x1 <= p[0] <= x2 and y1 <= p[1] <= y2:
            count += 1
    if count >= K:
        ans = min((x2-x1) * (y2-y1), ans)

print(ans)