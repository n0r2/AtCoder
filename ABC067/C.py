N = int(input())
a = list(map(int, input().split()))

arai = sum(a)-a[0]
sunuke = a[0]
ans = abs(sunuke-arai)
for i in a[1:-1]:
    sunuke += i
    arai -= i
    ans = min(abs(sunuke-arai), ans)

print(ans)