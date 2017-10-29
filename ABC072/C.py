from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)

ans = 0
for i in range(max(A)+1):
    ans = max(C[i] + C[i-1] + C[i+1], ans)

print(ans)
