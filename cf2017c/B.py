N = int(input())
t = 1
for i in map(int, input().split()):
    if i % 2 == 0:
        t *= 2
print(3**N-t)
