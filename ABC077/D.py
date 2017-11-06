def s(n):
    ret = 0
    sn = str(n)
    for c in sn:
        ret += int(c)
    return ret

N = int(input())
t = N

ans = s(N)
for i in range(1, 700000):
    if i%10 == 0:
        continue
    t = i*N
    ans = min(s(t), ans)

print(ans)