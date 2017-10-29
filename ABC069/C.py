N = int(input())
c = [0, 0, 0]  # 0, 2, 4

for i in map(int, input().split()):
    if i % 4 == 0:
        c[2] += 1
    elif i % 2 == 0:
        c[1] += 1
    else:
        c[0] += 1

if c[0] <= c[2] + (c[1] == 0):
    print('Yes')
else:
    print('No')