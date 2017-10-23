s = input()

i, j = 0, len(s)-1
ans = 0
while i < j:
    if s[i] == s[j]:
        i, j = i+1, j-1
    elif s[i] == 'x':
        i += 1
        ans += 1
    elif s[j] == 'x':
        j -= 1
        ans += 1
    else:
        ans = -1
        break

print(ans)