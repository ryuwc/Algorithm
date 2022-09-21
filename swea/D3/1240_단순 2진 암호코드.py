import sys; sys.stdin = open('input_단순2진암호코드.txt', 'r')


codes = [
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1],
]

for tc in range(int(input())):
    M, N = map(int, input().split())
    maps = []
    for _ in range(M):
        tmp = list(map(int, input()))
        if sum(tmp) != 0:
            if not maps:
                maps += tmp

    password = []
    for i in range(N-1, -1, -1):
        if maps[i] == 1:
            for j in range(i, i-56, -1):
                password.append(maps[j])
            break

    pwd = password[::-1]
    pwd_idx = []
    for i in range(0, 56, 7):
        for j in range(10):
            if pwd[i:i+7] == codes[j]:
                pwd_idx.append(j)

    hol = []
    zza = []
    for i in range(0, len(pwd_idx), 2):
        a, b = pwd_idx[i], pwd_idx[i+1]
        hol.append(a)
        zza.append(b)

    check = (sum(hol) * 3) + sum(zza)

    if check % 10 == 0:
        print(f'#{tc+1}', sum(pwd_idx))
    else:
        print(f'#{tc+1}', 0)
