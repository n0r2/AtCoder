from collections import Counter

N = int(input())
D = [int(i) for i in input().split()]
M = int(input())
T = [int(i) for i in input().split()]

d = Counter(D)
t = Counter(T)

for k, v in t.items():
    if d[k] < v:
        print('NO')
        break
else:
    print('YES')