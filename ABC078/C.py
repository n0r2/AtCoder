N, M = map(int, input().split())

time = (N-M) * 100 + M * 1900

ans = 0
for j in range(1, 10000):
    ans += time * j / (2**j)

print(int(round((ans*2**(M-1)), 5)))