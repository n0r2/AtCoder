S_ = input()
T = input()

for i in range(len(S_) - len(T), -1, -1):
    for j in range(len(T)):
        if S_[i + j] != '?' and S_[i + j] != T[j]:
            break
    else:
        print((S_[:i] + T + S_[i + len(T):]).replace('?', 'a'))
        break
else:
    print('UNRESTORABLE')
