from math import factorial


N, M = map(int, input().split())

p = abs(N-M)
if p > 1:
    ans = 0
else:
    if p == 0:
        ans = 2
    else:
        ans = 1
    for i in range(1, N+1):
        ans *= i
        ans %= 1000000007
    for i in range(1, M+1):
        ans *= i
        ans %= 1000000007

print(ans)
