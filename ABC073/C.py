from collections import Counter

N = int(input())
A = [int(input()) for i in range(N)]

c = Counter(A)

ans = 0
for a, b in c.items():
    if b % 2 == 1:
        ans += 1

print(ans)