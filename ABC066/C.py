n = int(input())
a = input().split()
print(" ".join(a[::2][::-1] + a[1::2] if n%2 else a[1::2][::-1] + a[::2]))
